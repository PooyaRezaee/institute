from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DetailView,ListView,FormView
from .models import News,Article,Handout
from accounts.models import Course,Poll,Choice,Vote
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseNotFound,HttpResponseForbidden

class Index(View):
    def get(self,request):
        last_news = News.objects.all().order_by('-created')[:5]
        last_articles = Article.objects.all().order_by('-created')[:5]
        last_handout = Handout.objects.all().order_by('-created')[:5]
        last_courses = Course.objects.all().order_by('-created')[:5]

        all_polls = None
        if request.user.is_authenticated:
            courses_user = request.user.courses.all()
            all_polls = Poll.objects.filter(Q(for_course__in=courses_user) & ~Q(votes__user=request.user))

        context = {
            'last_news':last_news,
            'last_articles':last_articles,
            'last_handout':last_handout,
            'last_courses':last_courses,
            'all_polls':all_polls,
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

class DetailPollView(LoginRequiredMixin,View):
    def dispatch(self, request,pk, *args, **kwargs):
        try:
            poll = Poll.objects.get(pk=pk)
            if Vote.objects.filter(poll=poll,user=request.user).exists():
                return HttpResponseForbidden()
        except:
            return HttpResponseNotFound()

        return super().dispatch(request,pk, *args, **kwargs)


    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        return render(
            request,
            template_name='home/detail_poll.html',
            context={
                "poll": poll,
            }
        )
    
    def post(self,request,pk):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=pk)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(
            poll=poll,
            choice=choice,
            user=request.user,
        )

        return redirect('home:index')