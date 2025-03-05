from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import Group

from .models import User, Teacher
from .forms import TeacherAddForm
from academics.models import Department
# Create your views here.
now = datetime.now()

class TeacherAddView(TemplateView):
    template_name = 'account/teacher_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeacherAddForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            department = Department.objects.get(id=data['department'].id)
            last_teacher = Teacher.objects.filter(department=department).select_related('user').order_by('-id').first()
            last_teacher_id = int(last_teacher.user.username.split('/')[-1]) if last_teacher else 0
            username = f'UNI/{department.code}/{now.year}/{last_teacher_id + 1}'
            try:
                user = User.objects.create_user(
                    username=username,
                    password='Summer@2025#',
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    phone=data['phone'],
                    gender=data['gender'],
                    blood_group=data['blood_group'],
                    present_address=data['present_address'],
                    permanent_address=data['permanent_address'],
                )
                user.groups.add(Group.objects.get(name='Teacher'))
                user.save()
                Teacher.objects.create(
                    user=user,
                    department=department,
                    designation=data['designation'],
                    qualification=data['qualification'],
                    experience=data['experience'],
                )
                messages.success(request, 'Teacher added successfully')
                return render(request, self.template_name, {'form': form})
            except IntegrityError:
                messages.error(request, 'Phone number already exists')
                return redirect('teacher_add')
        else:
            print(form.errors)
        
        return render(request, self.template_name, {'form': form})
