# services/views.py

from django.views.generic import ListView, DetailView
from .models import ServiceCategory, Service


class ServiceCategoryListView(ListView):
    model = ServiceCategory
    template_name = 'services/category_list.html'


class ServiceCategoryDetailView(DetailView):
    model = ServiceCategory
    template_name = 'services/category_detail.html'


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'


