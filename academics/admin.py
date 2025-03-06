from django.contrib import admin

from .models import Department, Course, AcademicYear
# # Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'max_year', 'level']

admin.site.register(Course, CourseAdmin)


admin.site.register(AcademicYear)