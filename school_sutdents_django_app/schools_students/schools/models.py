from django.db import models
from django.contrib import admin

# Create your models here.
class School(models.Model):
    
    school_choices =(('private_school','Private_school'),('state_school','State_school'))
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=250)
    
    school_type = models.CharField(max_length=30,choices=school_choices)
    
    
    
    def __str__(self):
        return f"School name: {self.school_name} and school address {self.school_address}"
    
    
admin.site.register(School)