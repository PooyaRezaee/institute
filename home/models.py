from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=64,verbose_name='عنوان')
    body = models.TextField(verbose_name='بدنه')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural  = 'اخبار'

class Article(models.Model):
    author = models.ForeignKey(User,related_name='article',verbose_name='نویسنده',on_delete=models.CASCADE)
    title = models.CharField(max_length=64,verbose_name='عنوان')
    body = models.TextField(verbose_name='متن مقاله')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural  = 'مقالات'