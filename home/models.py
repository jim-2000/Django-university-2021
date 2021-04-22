from django.db import models
from django.utils import timezone

# Create your models here.>>>>>>>>>>>>>>>>>>
class Courses(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'published')
    )
    COURSE_DURATION = [
        ('Month', 'Month'),
        ('Year', 'Year'),
    ]
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    courses_details = models.TextField()
    video = models.FileField(upload_to='course/videos/')
    imag_front = models.ImageField(upload_to='course_img/')
    imag_back = models.ImageField(upload_to='course_img/')
    imag_top= models.ImageField(upload_to='course_img/',blank=True, null=True)
    courses_type = models.CharField(max_length=22, choices=COURSE_DURATION, default='Month')
    courses_duration = models.CharField(max_length=20)
    publish = models.DateTimeField(default=timezone.now)
    created_course = models.DateField(auto_now_add=True)
    updated_course = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.course_name


class AdmissionForm(models.Model):
    student_Status = [
        ('New', 'New'),
        ('Cancelled', 'Cancelled'),
        ('Approved', 'Approved'),
    ]
    student_gender= [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    Married_Student= [
        ('Marred', 'Marred'),
        ('Unmarred', 'Unmarred'),
    ]
    EDUCATION_QUALIFICATION_OF_STUDENT= [
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
    ]
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, choices=student_Status, default='New')
    name = models.CharField(max_length=300)
    father_name = models.CharField(max_length=300)
    mother_name = models.CharField(max_length=300)
    gender = models.CharField(max_length=25, choices=student_gender, default='Male')
    maritial_status  = models.CharField(max_length=50, choices=Married_Student, default='Unmarred')
    Districk = models.CharField(max_length=100)
    Post_office = models.CharField(max_length=100)
    Village = models.CharField(max_length=100)
    Birthday = models.CharField(max_length=100)
    Education_qualification = models.CharField(max_length=100, choices=EDUCATION_QUALIFICATION_OF_STUDENT, default='SSC')
    Subject = models.ForeignKey(Courses,on_delete=models.CASCADE)
    student_img = models.ImageField(upload_to = 'student/student_img')
    mobileNumber = models.CharField(max_length=15, default='+880 ')
    email = models.EmailField(max_length=55, default='some@gmail.com')
    Created = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.name
    
    
