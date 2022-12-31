# Generated by Django 4.1.3 on 2022-12-31 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'خبر', 'verbose_name_plural': 'اخبار'},
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=64, verbose_name='عنوان'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('body', models.TextField(verbose_name='متن مقاله')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
        ),
    ]