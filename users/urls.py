from users.apps import UsersConfig
from django.urls import path
from users.views import LoginView, RegisterView, ProfileView, PasswordRecoveryView, verification_view, \
    CustomPasswordChangeView
from django.contrib.auth.views import LogoutView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('verification/', verification_view, name='verification'),

]