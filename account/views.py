from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import Group

from .models import User
from .forms import TeacherAddForm
# Create your views here.
now = datetime.now()

class TeacherAddView(TemplateView):
    template_name = 'account/teacher_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeacherAddForm()
        return context
    