from datetime import datetime
import csv
import random

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import Group

from .models import User, Teacher, Student
from .forms import TeacherAddForm, SignInForm, StudentAddForm
from academics.models import Department, Course
# Create your views here.

class SignInView(LoginView):
    template_name = 'account/sign_in.html'
    redirect_authenticated_user = True
    form_class = SignInForm



class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'

class TeacherAddView(TemplateView):
    template_name = 'account/teacher_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeacherAddForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            data = form.cleaned_data
            department = Department.objects.get(id=data['department'].id)
            last_teacher = Teacher.objects.filter(department=department).select_related('user').order_by('-id').first()
            last_teacher_id = int(last_teacher.user.username.split('/')[-1]) if last_teacher else 0
            username = f'GCU/{department.code}/{now.year}/{(last_teacher_id + 1):03d}'
            dob = data['date_of_birth']
            full_name = f"{data['first_name']}{data['last_name']}".lower()
            password = f"{full_name[:4]}{dob:%d%m}"
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    phone=data['phone'],
                    gender=data['gender'],
                    blood_group=data['blood_group'],
                    date_of_birth=data['date_of_birth'],
                    present_address=data['present_address'],
                    permanent_address=data['permanent_address'],
                    type='TE'
                )
                group, created = Group.objects.get_or_create(name='Teacher')
                user.groups.add(group)
                user.save()
                Teacher.objects.create(
                    user=user,
                    department=department,
                    designation=data['designation'],
                    qualification=data['qualification'],
                    experience=data['experience'],
                    specialization=data['specialization']
                )
                messages.success(request, 'Teacher added successfully')
                return render(request, self.template_name, {'form': form})
            except IntegrityError:
                messages.error(request, 'Phone number already exists')
                return render(request, self.template_name, {'form': form})
        else:
            print(form.errors)
        
        return render(request, self.template_name, {'form': form})

class TeacherListView(TemplateView):
    template_name = 'account/teacher_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.select_related('user')
        context['teachers'] = teachers
        return context

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please Select a CSV file')

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        now = datetime.now()
        for row in reader:
            department = Department.objects.get(code=row['department'])

            last_teacher = Teacher.objects.filter(department=department).select_related('user').order_by('-id').first()
            last_teacher_id = int(last_teacher.user.username.split('/')[-1]) if last_teacher else 0
            username = f'GCU/{department.code}/{now.year}/{(last_teacher_id + 1):03d}'
            dob = datetime.strptime(row["date_of_birth"], "%Y-%m-%d").date()
            full_name = f"{row['first_name']}{row['last_name']}".lower()
            password = f"{full_name[:4]}{dob:%d%m}"
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    phone=row['phone'],
                    gender=row['gender'],
                    blood_group=row['blood_group'],
                    date_of_birth=row['date_of_birth'],
                    present_address=row['present_address'],
                    permanent_address=row['permanent_address'],
                    type='TE'
                )
                group, created = Group.objects.get_or_create(name='Teacher')
                user.groups.add(group)
                user.save()
                Teacher.objects.create(
                    user=user,
                    department=department,
                    designation=row['designation'],
                    qualification=row['qualification'],
                    experience=row['experience'],
                    specialization=row['specialization']
                )
            except IntegrityError:
                messages.error(request, 'Somthing went wrong')


        return render(request, self.template_name)
    
class StudentAddView(TemplateView):
    template_name = 'account/student_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentAddForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = StudentAddForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            course = data['course']
            full_name = f"{first_name}{last_name}".lower()
            password = f"{full_name[:4]}{now:%d%m}"
            last_student = Student.objects.filter(course=course).select_related('user').order_by('-id').first()
            last_student_id = int(last_student.user.username.split('/')[-1]) if last_student else 0
            username = f'GCU/{course.code}/{now.year}/{(last_student_id + 1):03d}'
            print(username)
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})