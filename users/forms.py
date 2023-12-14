from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField(label='Введите ваш Email')


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=6, label='Код верификации')
