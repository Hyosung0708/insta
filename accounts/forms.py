from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'profile_image')


class CustomAuthenticationForm(AuthenticationForm):
    pass


class CustomProfileForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', )