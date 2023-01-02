from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import RegisterView,ProfileView,RequestTeacherView,CourseCreateView

app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("teacher/request/", RequestTeacherView.as_view(), name="teacher-request"),
    path("teacher/course/craete/", CourseCreateView.as_view(), name="create-course"),
]
