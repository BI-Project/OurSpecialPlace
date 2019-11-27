from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import View
from rest_framework import mixins, generics

from place.models import Place
from place.serializer import PlaceSerializer
from recommendation.src import Spot_list
from recommendation.src.MakeResult import FunctionBox
from CollaborativeFiltering.collaborative_filtering import CollaborativeFiltering

login_url = reverse_lazy('accounts:login')


class PlaceChoiceListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all().order_by('?')[:20]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# @method_decorator(login_required(login_url=login_url))
class PlaceChoiceTemplateView(TemplateView):
    template_name = 'place/index.html'


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
        result_list.append(int(request.POST.get('dormitory_hotel')))
        result_list.append(int(request.POST.get('day_N_night')))
        result_list.append(int(request.POST.get('age')))

        topten = FunctionBox(result_list, Spot_list.data_list)
        topten.CosSimilarity()
        result = topten.Ranking() #return dict
        key_list = []
        result_dict = {}
        for key in result.keys():
            place_object = get_object_or_404(Place, name=key)
            result_dict[key] = [(str(place_object.picture)), place_object.name, place_object.pk, place_object.comment]
            place_object.liked_user.add(request.user)
        context = {'message': result_dict}
        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})


class UserStarReceiveView(View):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        place_name = request.POST.get('name')
        star = request.POST.get('star')
        user = request.user
        user_place_dict = {}
        place_star_dict = {}
        place_star_dict[place_name] = int(star)
        user_place_dict[user] = place_star_dict

        collabo = CollaborativeFiltering(user_place_dict)

        context = {'message': collabo.user_reommendations(user)}

        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})
