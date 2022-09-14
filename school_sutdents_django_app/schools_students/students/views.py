from typing import List
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from students.serializers import StudentSerializer


from students.models import Student
from students.forms import StudentForm

class StudentListView(ListView):
    template_name = 'students/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    
    def get_queryset(self):
        return Student.objects.all()
    
    
class StudentCreateView(CreateView):
    template_name = 'students/create_student.html' #specificam calea catre fisierul html unde vom avea un fromular
    model = Student
    form_class = StudentForm

    success_url = reverse_lazy('home') #dupa salvarea datelor din formular vom fii redirectionati catre pagina home
   

class StudentViewSet(viewsets.ModelViewSet):
    """
    Api endpoint for the students
    """
    queryset = Student.objects.all()
    
    
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]