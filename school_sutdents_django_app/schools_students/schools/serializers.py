from rest_framework import serializers
from schools.models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        
        fields = ['school_name','school_address','school_type']