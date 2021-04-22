from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username
    

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username