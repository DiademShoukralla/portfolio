from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, UserChangeForm
from django.forms import TextInput, EmailInput, PasswordInput, CharField, EmailField
from django.template.defaultfilters import capfirst

from authen.models import User


class RegisterForm(UserCreationForm):
    """Authentication sign up form."""
    email = EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            'email': EmailInput(attrs={'autocomplete': 'off'}),
            'username': TextInput(attrs={'autocomplete': 'off'}),
            'password1': PasswordInput(attrs={'autocomplete': 'off'}),
            'password2': PasswordInput(attrs={'autocomplete': 'off'}),
        }


class LoginForm(AuthenticationForm):
    """Authentication log in form."""
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = "Username or Email"


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
