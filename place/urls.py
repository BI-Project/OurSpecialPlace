from django.urls import path
from .views import PlaceChoiceListView, PlaceChoiceTemplateView, ThanksTemplateView


app_name = 'place'

urlpatterns = [
    path('choice/', PlaceChoiceTemplateView.as_view(), name='choice'),
    path('ListAPI', PlaceChoiceListView.as_view(), name='list_api'),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),
]