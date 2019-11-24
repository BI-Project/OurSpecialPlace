from django.shortcuts import render
from place.models import Place
from django.views.generic import TemplateView
from rest_framework import mixins, generics
from place.serializer import PlaceSerializer


class PlaceChoiceListView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all().order_by('?')[:20]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PlaceChoiceTemplateView(TemplateView):
    template_name = 'place/index.html'
