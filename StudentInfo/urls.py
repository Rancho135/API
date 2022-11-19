from django.urls import path
from .import views
urlpatterns = [
    path('Student/<int:StudentId>', views.StudentInfo_detail),
    path('Students/', views.StudentInfo_all),
    path('StudentsRange/range', views.StudentInfo_range),
    
    
]