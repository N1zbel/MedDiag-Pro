from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at',)
    search_fields = ('author', 'content',)
    date_hierarchy = 'created_at'
    actions = ['delete_selected']


admin.site.register(Review, ReviewAdmin)
