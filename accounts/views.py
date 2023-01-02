from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView,UpdateView,RedirectView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseForbidden,HttpResponseNotFound
from .forms import ProfileForm,CourseCreationForm
from accounts.models import Teacher,Course
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

class CourseCreateView(CreateView):
    def dispatch(self, request, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(account=request.user)
        except:
            return HttpResponseForbidden()
        if teacher.is_active:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()


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