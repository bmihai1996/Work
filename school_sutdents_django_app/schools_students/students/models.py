from django.db import models
from django.contrib import admin
# Create your models here.
from schools.models import School
class Student(models.Model):
    
    gender_choices = (('male','Male'),('female','Female'))
    
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_olympic = models.BooleanField(default=False)
    email = models.EmailField(max_length=40)
    description = models.TextField(max_length=1000)
    
    gender = models.CharField(max_length=20, choices=gender_choices)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def get_full_name(self):
         return str(self)
     
admin.site.register(Student)