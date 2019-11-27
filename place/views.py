from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import mixins, generics

from place.models import Place
from place.serializer import PlaceSerializer

from place.models import UserPlaceStar

import json
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
        pass

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
        key_list = []
        result_dict = {}
        for key in result.keys():
            place_object = get_object_or_404(Place, name=key)
            result_dict[key] = [(str(place_object.picture.url)), place_object.name, place_object.pk, place_object.comment]
            # place_object.liked_user.add(request.user)
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

        place = get_object_or_404(Place, pk=pk)

        user_place = UserPlaceStar(user=request.user, place=place, star=star)
        user_place.save()

        UserPlaceStar.objects.filter(place=place_name)



        collabo = CollaborativeFiltering(user_place_dict)

        context = {'message': collabo.user_reommendations(user)}

        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})