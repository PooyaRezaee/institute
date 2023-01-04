from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Teacher
from django.http import HttpResponseForbidden

class TeacherLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(account=request.user)
        except:
            return HttpResponseForbidden()
        if teacher.is_active:
                return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()