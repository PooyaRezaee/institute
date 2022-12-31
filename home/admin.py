from django.contrib import admin
from .models import News,Article,Handout

@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title','created')

@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')

@admin.register(Handout)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title','created')