# Generated by Django 4.1.3 on 2023-01-04 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_poll_for_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'گزینه', 'verbose_name_plural': 'گزینه ها'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'نظرسنجی', 'verbose_name_plural': 'نظرسنجی ها'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'رای', 'verbose_name_plural': 'رای ها'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(max_length=20, verbose_name='نام گزینه'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='choices',
            field=models.ManyToManyField(related_name='poll', to='accounts.choice', verbose_name='گزینه ها'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='for_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='accounts.course', verbose_name='برای دوره'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.CharField(max_length=64, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='accounts.teacher', verbose_name='مالک'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='accounts.choice', verbose_name='گزینه'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='accounts.poll', verbose_name='نظرسنجی'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
