from django.urls import path
from .views import Index,DetailNewsView

app_name = 'home'

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("news/<int:pk>/", DetailNewsView.as_view(), name="detail-news"),
]
