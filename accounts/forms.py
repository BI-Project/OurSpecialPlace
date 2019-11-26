from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms
from .models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'age',
        )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(UserCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        ret = super(UserCreateForm, self).save(commit)
        if commit:
            self.user = authenticate(
                self.request,
                username=self.cleaned_data.get('username'),
                password=self.cleaned_data.get('password2')
            )
        return ret


class CustomizedAutenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 0:
            raise forms.ValidationError("The user does not exist")
        else:
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is no longer active")
        return super(CustomizedAutenticationForm, self).clean()
