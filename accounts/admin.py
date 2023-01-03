from django.contrib import admin
from .models import Teacher,Course,Poll,Choice,Vote


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('account','is_active','request_at')

@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('name','teacher','created')
    
@admin.register(Poll)
class PollModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class VoteModelAdmin(admin.ModelAdmin):
    pass