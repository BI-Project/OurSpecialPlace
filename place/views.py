from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.views.generic import TemplateView
from django.views.generic import View
from rest_framework import mixins, generics

from place.models import Place
from place.serializer import PlaceSerializer
from recommendation.src import Spot_list
from recommendation.src.MakeResult import FunctionBox

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


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


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
            result_dict[key] = serialize('json', get_object_or_404(Place, name=key), cls=LazyEncoder)
        context = {'message': result_dict}
        return JsonResponse(context, json_dumps_params={'ensure_ascii': True})

