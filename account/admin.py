from django.contrib import admin

from .models import User, Teacher
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(User, UserAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation')

admin.site.register(Teacher, TeacherAdmin)

