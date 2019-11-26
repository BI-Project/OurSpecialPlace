from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import mixins, generics

from place.models import Place
from place.serializer import PlaceSerializer

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
