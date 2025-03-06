from hashids import Hashids

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

hashids = Hashids(salt='change_user_id', min_length=10)
# Create your models here.
class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[\w@.+\-\/]+$',
        message='Username must be Alphanumeric',
    )
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]
    
    USER_TYPE_CHOICES = [
        ('AD', 'Admin'),
        ('TE', 'Teacher'),
        ('ST', 'Student'),
        ('SF', 'Staff'),
    ]
    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    present_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default='ST')
    profile_color = models.CharField(max_length=10, default='#007bff', null=True, blank=True)

    def __str__(self):
        return self.username
    
    def get_first_letter(self):
        return f'{self.first_name[:1]}'
    
    def get_hash_id(self):
        return hashids.encode(self.id)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    sem = models.CharField(max_length=2, default='1')
    admission_date = models.DateField(null=True, blank=True)
    class_roll = models.CharField(max_length=5, verbose_name='Class Roll Number')
    uni_roll = models.CharField(max_length=10, unique=True, null=True, verbose_name='University Roll Number')
    reg_number = models.CharField(max_length=10, unique=True, null=True, verbose_name='Registration Number')

    guardian_name = models.CharField(max_length=100, null=True, verbose_name="Guardian's Name")
    guardian_contact = models.CharField(max_length=15, null=True, verbose_name="Guardian's Contact")

    age_proof = models.FileField(upload_to='student/documet/', null=True, blank=True)
    address_proof = models.FileField(upload_to='student/documet/', null=True, blank=True)
    
    def __str__(self):
        return self.user.username