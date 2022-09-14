from django import forms
from django.forms import TextInput, Select, TimeInput

from schools.models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','school_address','school_type']
        
        widgets = {
            'school_name':TextInput(attrs={'placeholder': 'Enter your school name', 'class': 'form-control'}),
            'school_address':TextInput(attrs={'placeholder': 'Enter your school address', 'class': 'form-control'}),
            'school_choices':Select(attrs={'class': 'form-control'}),
        }