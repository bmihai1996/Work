from .views import DrinkList
from rest_framework.routers import DefaultRouter

from django.urls import path,include

urlpatterns = [
    path('drinks/',DrinkList.as_view())
]