from django.contrib import admin
from .models import News

@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title','created')