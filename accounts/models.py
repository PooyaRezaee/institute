from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=64,verbose_name='اسم دوره',unique=True)
    thumbnail = models.ImageField(upload_to='course',verbose_name='تصویر')
    description = models.CharField(max_length=256,verbose_name='توضیحات')
    teacher = models.ForeignKey('Teacher',models.CASCADE,verbose_name='استاد دوره')
    start = models.DateField(verbose_name='تاریخ شروع دوره')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    members = models.ManyToManyField(User,related_name='courses')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural  = 'دوره ها'

class Teacher(models.Model):
    account = models.OneToOneField(User,on_delete=models.CASCADE,related_name='teacher',verbose_name='حساب کاربری استاد')
    is_active = models.BooleanField(default=False,verbose_name='فعال بودن')
    request_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ درخواست')

    def __str__(self):
        return self.account.username
    
    class Meta:
        verbose_name = 'مدرس'
        verbose_name_plural  = 'مدرسان'

class Choice(models.Model):
    name = models.CharField(max_length=20,verbose_name='نام گزینه')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'گزینه'
        verbose_name_plural  = 'گزینه ها'

class Poll(models.Model):
    name = models.CharField(max_length=64,verbose_name='عنوان')
    choices = models.ManyToManyField(Choice, related_name='poll',verbose_name='گزینه ها')
    owner = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='polls',verbose_name='مالک')
    for_course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='polls',verbose_name='برای دوره')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نظرسنجی'
        verbose_name_plural  = 'نظرسنجی ها'

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True,verbose_name='نظرسنجی')
    choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True,verbose_name='گزینه')
    user = models.ForeignKey(User,on_delete=models.SET_NULL, related_name="votes", null=True, blank=True,verbose_name='کاربر')

    def __str__(self):
        return f"{self.poll.name} - {self.choice.name}"
    
    class Meta:
        verbose_name = 'رای'
        verbose_name_plural  = 'رای ها'