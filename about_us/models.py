from django.db import models


class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name='Имя')
    content = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
