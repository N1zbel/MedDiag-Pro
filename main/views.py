from django.shortcuts import render, redirect
import json
from django.http import JsonResponse

from main.models import Contact
from services.models import Service, ServiceCategory


def home(request):
    context = {
        'title': 'Домашняя страница'
    }
    return render(request, 'main/home.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact_message = Contact.objects.create(name=name, phone=phone, message=message)

        return redirect('/')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', context)


def write_data_to_json(request):
    services = list(Service.objects.values())
    categories = list(ServiceCategory.objects.values())

    data = {"services": services, "categories": categories}

    json_file_path = "main/data.json"
    with open(json_file_path, 'w', encoding='UTF-8') as formatted_file:
        json.dump(data, formatted_file, ensure_ascii=False, indent=2)

    return JsonResponse({"status": "success"})
