from django.urls import path
from django.views.decorators.cache import cache_page


from main.views import home, contacts, write_data_to_json

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('write_data_to_json/', write_data_to_json, name='write_data_to_json'),
]