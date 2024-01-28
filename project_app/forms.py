# project_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    start_date = forms.DateTimeField(input_formats=["%d/%m/%y"])
    estimated_end_date = forms.DateTimeField(input_formats=["%d/%m/%y"])
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'estimated_end_date']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'mobile_number')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status']
