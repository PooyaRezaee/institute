from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseForbidden
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
        return redirect('accounts:profile')