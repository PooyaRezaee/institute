from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView,ListView
from .models import News,Article,Handout
from accounts.models import Course
class Index(View):
    def get(self,request):
        last_news = News.objects.all().order_by('-created')[:5]
        last_articles = Article.objects.all().order_by('-created')[:5]
        last_handout = Handout.objects.all().order_by('-created')[:5]
        last_courses = Course.objects.all().order_by('-created')[:5]

        context = {
            'last_news':last_news,
            'last_articles':last_articles,
            'last_handout':last_handout,
            'last_courses':last_courses,
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

class DetailArticleView(DetailView):
    template_name = 'home/detail_article.html'
    model = Article
    context_object_name = 'article'

class ArticleListView(ListView):
    template_name = 'home/list_article.html'
    model = Article
    context_object_name = 'all_articles'

class HandoutListView(ListView):
    template_name = 'home/list_handout.html'
    model = Handout
    context_object_name = 'all_handout'

class CourseListView(ListView):
    template_name = 'home/list_course.html'
    model = Course
    context_object_name = 'all_courses'

class DetailCourseView(DetailView):
    template_name = 'home/detail_course.html'
    model = Course
    context_object_name = 'course'