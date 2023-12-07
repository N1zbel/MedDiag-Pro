from django.urls import path
from django.views.decorators.cache import cache_page


from main.views import home, contacts, about, services

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
]