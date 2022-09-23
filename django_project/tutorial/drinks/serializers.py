
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
        
