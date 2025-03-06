from django import forms
from django.contrib.auth.forms import AuthenticationForm

from academics.models import Department, Course

class UserAddForm(forms.Form):
    GENDER_CHOICES = (
        ('', '--Select Gender--'),
        ('M', 'Male'),
        ('F', 'Female'),
        # ('O', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('', '--Select Blood Group--'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}))
    gender = forms.CharField(max_length=2, widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'select', 'placeholder': 'Gender'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'type': 'date'}))
    blood_group = forms.CharField(max_length=5, widget=forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class': 'select', 'placeholder': 'Date of Birth'}))
    present_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Present Address'}))
    permanent_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Permanent Address'}))

class TeacherAddForm(UserAddForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Department'}))
    designation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Designation'}))
    qualification = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Qualification'}))
    experience = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Experience'}))
    specialization = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Specialization'}))


class StudentAddForm(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'select'}))



class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))