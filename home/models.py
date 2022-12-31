from django.db import models

class News(models.Model):
    title = models.CharField(max_length=64,verbose_name='عنوان')
    body = models.TextField(verbose_name='بدنه')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural  = 'اخبار'