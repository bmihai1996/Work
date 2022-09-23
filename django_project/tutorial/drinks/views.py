
from django.contrib.auth.models import User
from .serializers import DrinkSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Drink

class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAdminUser]