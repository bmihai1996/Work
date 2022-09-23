from django.contrib import admin
from .models import Drink


class DrinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Drink)
