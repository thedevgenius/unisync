from django.contrib import admin

from .models import User, Teacher
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return obj.get_full_name()

    list_display = ('username', 'full_name', 'email', 'type', 'profile_color')

admin.site.register(User, UserAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation')

admin.site.register(Teacher, TeacherAdmin)



