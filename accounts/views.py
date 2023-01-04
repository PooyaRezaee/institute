from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView,UpdateView,RedirectView,DeleteView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseForbidden,HttpResponseNotFound
from .forms import CourseCreationForm,ArticleCreationForm,HandoutCreationForm,PollCreationForm,ChoiceAddForm
from .models import Teacher,Course,Poll,Choice
from home.models import Article,Handout
from .mixins import TeacherLoginRequiredMixin

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')

class ProfileView(LoginRequiredMixin,UpdateView):
    template_name = 'account/profile.html'
    success_url = reverse_lazy('accounts:profile')
    model = User
    fields = ('username','email','first_name','last_name')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

class RequestTeacherView(LoginRequiredMixin,RedirectView):
    url = reverse_lazy('accounts:profile')

    def get_redirect_url(self):
        try:
            Teacher.objects.create(account=self.request.user)
        except:
            pass
        return super().get_redirect_url()

class CourseCreateView(TeacherLoginRequiredMixin,CreateView):
    template_name = 'account/craete_course.html'
    form_class = CourseCreationForm

    def form_valid(self, form):
        cd = form.cleaned_data
        Course.objects.create(**cd,teacher=self.request.user.teacher)
        return redirect('accounts:list-courses')

class MyCoursesView(LoginRequiredMixin,View):
    def get(self,request,course_id=None):
        if course_id:
            try:
                course = Course.objects.get(pk=course_id)
            except:
                return HttpResponseNotFound()
            
            if not course in request.user.courses.all():
                course.members.add(request.user)
        try:
            teacher = Teacher.objects.get(account=request.user)
            is_teacher = True
            course_list = Course.objects.filter(teacher=teacher)
        except:
            user = request.user
            is_teacher = False
            course_list = user.courses.all()

        context = {
            'is_teacher':is_teacher,
            'course_list':course_list,
        }

        return render(request,'account/courses.html',context)

class LeaveCourse(LoginRequiredMixin,View):
    def get(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return HttpResponseNotFound()
        
        try:
            course.members.remove(request.user)
        except:
            return HttpResponseNotFound()

        return redirect('accounts:list-courses')

class DeleteCourse(LoginRequiredMixin,View):
    def dispatch(self, request,pk, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(account=request.user)
            course = Course.objects.get(pk=pk,teacher=teacher)
        except:
            return HttpResponseForbidden()
        if teacher.is_active:
            return super().dispatch(request,pk, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    
    def get(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return HttpResponseNotFound()
        
        course.delete()
        return redirect('accounts:list-courses')

class CreateArticleView(LoginRequiredMixin,CreateView):
    template_name = 'account/craete_article.html'
    form_class = ArticleCreationForm

    def form_valid(self, form):
        cd = form.cleaned_data
        Article.objects.create(**cd,author=self.request.user)
        return redirect('accounts:list-articles')

class ArticleListView(LoginRequiredMixin,ListView):
    template_name = 'account/articles.html'
    context_object_name = 'list_articles'

    def get_queryset(self):
        queryset = Article.objects.filter(author=self.request.user)
        return queryset

class DeleteArticleView(LoginRequiredMixin,View):
    def dispatch(self, request,pk, *args, **kwargs):
        try:
            article = Article.objects.get(pk=pk,author=self.request.user)
        except:
            return HttpResponseForbidden()

        return super().dispatch(request,pk, *args, **kwargs)

    
    def get(self,request,pk):
        try:
            article = Article.objects.get(pk=pk)
        except:
            return HttpResponseNotFound()
        
        article.delete()
        return redirect('accounts:list-articles')

class CreateHandoutView(TeacherLoginRequiredMixin,CreateView):
    template_name = 'account/craete_handout.html'
    form_class = HandoutCreationForm

    def form_valid(self, form):
        cd = form.cleaned_data
        Handout.objects.create(**cd)
        return redirect('home:index')

class PollListView(TeacherLoginRequiredMixin,ListView):    
    template_name = 'account/polls.html'
    context_object_name = 'list_polls'

    def get_queryset(self):
        queryset = Poll.objects.filter(owner=self.request.user.teacher)
        return queryset

class CreatePollView(TeacherLoginRequiredMixin,View):
    form_class = PollCreationForm

    def get(self,request):
        return render(request,'account/create_poll.html',{'form':self.form_class})
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)

        if form.is_valid():
            cd = form.cleaned_data
            Poll.objects.create(
                name=cd['name'],
                for_course=cd['for_course'],
                owner=request.user.teacher,
                )
            return redirect('accounts:list-poll')

        return render(request,'account/create_poll.html',{'form':form})

class AddChoiceView(TeacherLoginRequiredMixin,View):
    form_class = ChoiceAddForm
    def get(self,request,poll_id):
        form = self.form_class

        return render(request,'account/create_poll.html',{'form':form})

    def post(self,request,poll_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            choice = Choice.objects.create(name=form.cleaned_data['name'])
            Poll.objects.get(id=poll_id).choices.add(choice)
            return redirect('accounts:list-poll')


        return render(request,'account/create_poll.html',{'form':form})