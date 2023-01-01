from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from .forms import ProfileForm
from accounts.models import Teacher

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