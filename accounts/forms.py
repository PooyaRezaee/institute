from django import forms
from django.contrib.auth.models import User
from .models import Course

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('teacher',)
        widgets = {
            'description': forms.Textarea(),
            'start': DateInput,
        }
