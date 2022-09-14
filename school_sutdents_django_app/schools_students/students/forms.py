from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateTimeInput, DateInput, Select

from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  #Formularul va contine toate fieldurile din modelul Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'email', 'description','gender','school']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Enter your description', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'school': Select(attrs={'class': 'form-control'}),
            
        }