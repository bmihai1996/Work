from django.urls import include, path


from students import views




urlpatterns = [
    path('list-of-students/',views.StudentListView.as_view(),name='list_of_students'),
    path('create-student/',views.StudentCreateView.as_view(),name='create_student')
]