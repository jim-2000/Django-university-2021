from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='HOME'),
    path('course/', views.Course, name='COURSE'),
    path('courses/<int:id>', views.CourseSingle, name='COURSES'),
    path('admission/', views.Admission, name='ADMISSION'),
    path('register/', views.RegisterUser, name='Register'),
    
]