from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView,ListView
from .models import News
class Index(View):
    def get(self,request):
        all_news = News.objects.all().order_by('-created')[:5]

        context = {
            'all_news':all_news,
        }

        return render(request,'home/index.html',context)

class DetailNewsView(DetailView):
    template_name = 'home/detail_news.html'
    model = News
    context_object_name = 'news'

class NewsListView(ListView):
    template_name = 'home/list_news.html'
    model = News
    context_object_name = 'all_news'