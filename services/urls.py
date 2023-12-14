from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('categories/', views.ServiceCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.ServiceCategoryDetailView.as_view(), name='category-detail'),
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]