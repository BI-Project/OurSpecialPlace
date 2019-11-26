from django.urls import path
from .views import PlaceChoiceListView, PlaceChoiceTemplateView


app_name = 'place'

urlpatterns = [
    path('choice/', PlaceChoiceTemplateView.as_view(), name='choice'),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),
    path('', PlaceChoiceListView.as_view(), name='list_api'),
    path('UserProfileReceiveAPI', UserProfileReceiveView.as_view(), name='user_profile_receive')
]