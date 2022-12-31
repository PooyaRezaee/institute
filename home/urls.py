from django.urls import path
from .views import Index,DetailNewsView,NewsListView,DetailArticleView,ArticleListView,HandoutListView

app_name = 'home'

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("news/<int:pk>/", DetailNewsView.as_view(), name="detail-news"),
    path("news/", NewsListView.as_view(), name="list-news"),
    path("article/<int:pk>/", DetailArticleView.as_view(), name="detail-article"),
    path("article/", ArticleListView.as_view(), name="list-article"),
    path("handout/", HandoutListView.as_view(), name="list-handout"),
]