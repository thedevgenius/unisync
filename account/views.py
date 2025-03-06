from datetime import datetime
from hashids import Hashids
import csv
import random

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import Group

from .models import User, Teacher, Student
from .forms import TeacherAddForm, SignInForm, StudentAddForm, GurdianForm, DocumentUploadForm
from academics.models import Department, Course
# Create your views here.
hashids = Hashids(salt='change_user_id', min_length=10)


class SignInView(LoginView):
    template_name = 'account/sign_in.html'
    redirect_authenticated_user = True
    form_class = SignInForm


class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all().select_related('user')
        return context
    


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
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=data['email'],
                phone=data['phone'],
            )
            group, created = Group.objects.get_or_create(name='Student')
            user.groups.add(group)
            user.save()
            Student.objects.create(
                user=user,
                course=course,
                sem='1',
                admission_date=now,
                class_roll=last_student_id + 1,
            )
            messages.success(request, 'Student added successfully')
            return redirect('complete_admission' , hash_id=user.get_hash_id())
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


class AdmissionCompleteView(FormView):
    template_name = 'account/admission_complete.html'
    def get(self, request, *args, **kwargs):
        """Handles GET request to display both forms."""
        try:
            hash_id = kwargs['hash_id']
            id = hashids.decode(hash_id)[0]
            student = Student.objects.get(user_id=id)
        except (IndexError, Student.DoesNotExist):
            messages.error(request, "Invalid student ID")
            return redirect("error_page")  # Redirect to an appropriate error page

        form = GurdianForm()
        form2 = DocumentUploadForm()

        return render(request, self.template_name, {"student": student, "form": form, "form2": form2})
    
    def post(self, request, *args, **kwargs):
        """Handles form submission for both forms."""
        try:
            student = Student.objects.get(user_id=hashids.decode(kwargs['hash_id'])[0])
        except (IndexError, Student.DoesNotExist):
            messages.error(request, "Invalid student ID")
            return redirect("error_page")

        form = GurdianForm(request.POST)
        form2 = DocumentUploadForm(request.POST, request.FILES)

        if "submit_form" in request.POST:
            if form.is_valid():
                student.guardian_name = form.cleaned_data["guardian_name"]
                student.guardian_contact = form.cleaned_data["guardian_contact"]
                student.save()
                messages.success(request, "Guardian added successfully")
                return redirect(request.path)  # Redirect to the same page (avoids duplicate form submissions)
            else:
                messages.error(request, "Error in Guardian Form")

        elif "submit_form2" in request.POST:
            if form2.is_valid():
                # Handle file upload logic here
                print(form2.cleaned_data)
                student.age_proof = form2.cleaned_data["age_proof"]
                student.address_proof = form2.cleaned_data["address_proof"]
                student.save()
                messages.success(request, "Document uploaded successfully")
                return redirect(request.path)
            else:
                messages.error(request, "Error in Document Upload Form")

        # If form validation fails, render the form with errors
        return render(request, self.template_name, {"student": student, "form": form, "form2": form2})
    
