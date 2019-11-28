from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import View
from rest_framework import mixins, generics

from place.models import Place, UserPlaceStar, TestPlace
from place.serializer import PlaceSerializer
from recommendation.src import Spot_list
from recommendation.src.MakeResult import FunctionBox
from CollaborativeFiltering.collaborative_filtering import CollaborativeFiltering

from accounts.models import User
import collections

login_url = reverse_lazy('accounts:login')


class PlaceChoiceListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = PlaceSerializer
    queryset = TestPlace.objects.all().order_by('?')[:20]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PlaceChoiceTemplateView(TemplateView):
    template_name = 'place/index.html'

    @method_decorator(login_required(login_url=login_url))
    def get(self, request, *args, **kwargs):
        return super(PlaceChoiceTemplateView, self).get(request, *args, **kwargs)


class IntroductionView(TemplateView):
    template_name = 'place/introduction.html'


class ThanksTemplateView(TemplateView):
    template_name = 'place/thanks.html'


class UserProfileReceiveView(View):

    def post(self, request, *args, **kwargs):
        result_list=[]

        result_list.append(int(request.POST.get('natural_city')))
        result_list.append(int(request.POST.get('static_dynamic')))
        result_list.append(int(request.POST.get('mountain_sea')))
        result_list.append(int(request.POST.get('history_modern')))
        result_list.append(int(request.POST.get('save_flex')))
        result_list.append(int(request.POST.get('accessibility')))
        result_list.append(int(request.POST.get('season')))
        result_list.append(int(request.POST.get('dormitory_hotel')))
        result_list.append(int(request.POST.get('day_N_night')))
        result_list.append(int(request.POST.get('age')))

        request.user.natural_city = int(request.POST.get('natural_city'))
        request.user.static_dynamic = int(request.POST.get('static_dynamic'))
        request.user.mountain_sea = int(request.POST.get('mountain_sea'))
        request.user.history_modern = int(request.POST.get('history_modern'))
        request.user.save_flex = int(request.POST.get('save_flex'))
        request.user.accessibility = int(request.POST.get('accessibility'))
        request.user.dormitory_hotel = int(request.POST.get('dormitory_hotel'))
        request.user.season = int(request.POST.get('season'))
        request.user.day_N_night = int(request.POST.get('day_N_night'))
        request.user.age = int(request.POST.get('age'))

        topten = FunctionBox(result_list, Spot_list.data_list)
        topten.CosSimilarity()
        result = topten.Ranking() #return dict
        result_dict = {}
        for key in result.keys():
            place_object = get_object_or_404(Place, name=key)
            result_dict[key] = [(str(place_object.picture.url)), place_object.name, place_object.pk, place_object.comment]
        context = {'message': result_dict}
        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})


class UserStarReceiveView(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        place_name = request.POST.get('name')
        star = request.POST.get('star')
        user_place_dict = {}
        place_star_dict = {}
        place_star_dict[place_name] = int(star)
        user_place_dict[request.user] = place_star_dict

        place = get_object_or_404(Place, pk=pk)

        user_place = UserPlaceStar(user=request.user, place=place, star=star)

        result_dict = collections.defaultdict(dict)
        user_place.save()
        qs= UserPlaceStar.objects.values()
        for i in qs:
            user_name = get_object_or_404(User, pk=i['user_id']).username
            place_name = get_object_or_404(Place, pk=i['place_id']).name
            place_star = i['star']
            result_dict[user_name][place_name] = place_star

        collabo = CollaborativeFiltering(result_dict)
        another_place = collabo.user_recommendations(request.user.username)
        context = {'message': another_place}

        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})