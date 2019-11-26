from django.urls import path
from .views import UserSignUpView, UserLoginView, UserLogoutView


app_name = 'accounts'

urlpatterns = [
    path('signup', UserSignUpView.as_view(), name='signup'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
]
