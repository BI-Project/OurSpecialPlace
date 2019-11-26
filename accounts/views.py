from .forms import CustomizedAutenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import FormView, CreateView, View
from .forms import UserCreateForm
from django.contrib.auth import login as auth_login, logout as auth_logout


class UserSignUpView(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/user_signup.html'
    success_url = reverse_lazy('place:choice')

    def get_form_kwargs(self):
        kwargs = super(UserSignUpView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        ret = super(UserSignUpView, self).form_valid(form)
        auth_login(self.request, form.user)
        return ret


class UserLogoutView(View):

    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(reverse_lazy('place:thanks'))

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class UserLoginView(FormView):
    form_class = CustomizedAutenticationForm
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy('place:choice')
