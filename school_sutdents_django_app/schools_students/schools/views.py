from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from schools.serializers import SchoolSerializer
from rest_framework import permissions
from schools.models import School
from schools.forms import SchoolForm
from students.models import Student



class SchoolListView(ListView):
    template_name = 'schools/list_of_schools.html'
    model  = School
    context_object_name = 'all_schools'
    
    
    def get_queryset(self):
        return School.objects.all()
    
    

class SchoolCreateView(CreateView):
    template_name = 'schools/create_school.html'
    model = School
    form_class = SchoolForm
    success_url = reverse_lazy('home')
    
    
    
    
class SchoolViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows schools to be viewed or edited.
    """
   
    queryset = School.objects.all()
    
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]