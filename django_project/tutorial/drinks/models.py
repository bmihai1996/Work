from django.db import models

# Create your models here.


class Drink(models.Model):
    
    
    DRINK_TYPES = (
        ('A','Alcoholic'),
        ('S','Soft'),
        ('T','Tonicdrink'),
    )
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    expiration_date = models.DateField()
    drink_choice = models.CharField(max_length=1,choices=DRINK_TYPES)
    
    
    
    def __str__(self):
        return f"{self.name}"