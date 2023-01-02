from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import RegisterView,ProfileView,RequestTeacherView,CourseCreateView,MyCoursesView,DeleteCourse,LeaveCourse,CreateArticleView,DeleteArticleView,ArticleListView,CreateHandoutView

app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("teacher/request/", RequestTeacherView.as_view(), name="teacher-request"),
    path("teacher/course/craete/", CourseCreateView.as_view(), name="create-course"),
    path("course/", MyCoursesView.as_view(), name="list-courses"),
    path("course/register/<int:course_id>/", MyCoursesView.as_view(), name="register-courses"),
    path("course/delete/<int:pk>/", DeleteCourse.as_view(), name="delete-course"),
    path("course/leave/<int:pk>/", LeaveCourse.as_view(), name="leave-course"),
    path("article/", ArticleListView.as_view(), name="list-articles"),
    path("article/create/", CreateArticleView.as_view(), name="create-article"),
    path("article/delete/<int:pk>/", DeleteArticleView.as_view(), name="delete-article"),
    path("handout/create/", CreateHandoutView.as_view(), name="create-handout"),
]
