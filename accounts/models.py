from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=64,verbose_name='اسم دوره')
    description = models.CharField(max_length=256,verbose_name='توضیحات')
    teacher = models.ForeignKey('Teacher',models.CASCADE,verbose_name='استاد دوره')
    start = models.DateField(verbose_name='تاریخ شروع دوره')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural  = 'دوره ها'

class Teacher(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher',unique=True,verbose_name='حساب کاربری استاد')
    is_active = models.BooleanField(default=False,verbose_name='فعال بودن')
    request_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ درخواست')

    def __str__(self):
        return self.account.username
    
    class Meta:
        verbose_name = 'مدرس'
        verbose_name_plural  = 'مدرسان'