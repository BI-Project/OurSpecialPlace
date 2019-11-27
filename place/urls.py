from django.urls import path
from .views import PlaceChoiceListView, PlaceChoiceTemplateView, ThanksTemplateView, \
    UserProfileReceiveView, UserStarReceiveView


app_name = 'place'

urlpatterns = [
    path('choice/', PlaceChoiceTemplateView.as_view(), name='choice'),
    path('ListAPI', PlaceChoiceListView.as_view(), name='list_api'),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),
    path('UserProfileReceiveAPI', UserProfileReceiveView.as_view(), name='user_profile_receive'),
    path('UserStarReceive', UserStarReceiveView.as_view(), name='user_star_receive')

]