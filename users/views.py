from django.contrib.auth.views import LoginView as BaseLoginView, PasswordChangeView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
import random
import string
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, UpdateView, FormView
from users.forms import UserRegisterForm, UserProfileForm, PasswordRecoveryForm, VerificationCodeForm, \
    CustomPasswordChangeForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    context_object_name = 'users'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        verification_code = ''.join(random.choice(string.digits) for _ in range(6))

        send_mail(
            'Код верификации',
            f'Ваш код верификации: {verification_code}',
            User.email,
            [form.cleaned_data['email']],
            fail_silently=False,
        )

        user = form.save(commit=False)
        user.verification_code = verification_code
        user.save()

        return redirect('users:verification')


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('main:home')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/users_form.html'

    def get_object(self, queryset=None):
        return self.request.user


class PasswordRecoveryView(FormView):
    form_class = PasswordRecoveryForm
    template_name = 'users/password_recovery.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        length = 16
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        password = get_random_string(length, alphabet)
        user.set_password(password)
        user.save()
        subject = 'Восстановление пароля'
        message = f'Ваш новый пароль: {password}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


def verification_view(request):
    if request.method == 'POST':
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verification_code']
            try:
                user = User.objects.get(verification_code=entered_code)
                if user:
                    user.is_verified_email = True
                    user.save()
                    return redirect('main:home')
            except User.DoesNotExist:
                form.add_error('verification_code', 'Пользователь с таким кодом верификации не найден')
    else:
        form = VerificationCodeForm()

    return render(request, 'users/verification.html', {'form': form})
