from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput,
        label='Nom d\'utilisateur',
        error_messages={
            'required': '',
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Mot de passe',
        error_messages={
            'required': '',
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirmer mod de passe',
        error_messages={
            'required': '',
        }
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
