from django.contrib import admin
from .models import Teacher,Course


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('account','is_active','request_at')

@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('name','teacher','created')