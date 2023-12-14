from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=50, verbose_name='Название услуги')
    price = models.IntegerField(verbose_name='Цена услуги')
    description = models.TextField(verbose_name='Описание услуги')

    def __str__(self):
        return self.name
