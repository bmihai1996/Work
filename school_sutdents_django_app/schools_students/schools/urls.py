from django.urls import path,include
from schools import views



urlpatterns = [
    path('list-of-schools/',views.SchoolListView.as_view(),name='list_of_schools'),
    path('create-school/',views.SchoolCreateView.as_view(),name='create_school')
]