from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[\w@.+\-\/]+$',
        message='Username must be Alphanumeric',
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        # ('O', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)    
    present_address = models.CharField(max_length=200, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, blank=True, null=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    

    def __str__(self):
        return self.username
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True, null=True)
    joining_date = models.DateField(null=True, blank=True)
    qualification = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username