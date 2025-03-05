from django.urls import path

from .views import TeacherAddView, TeacherListView, SignInView, DashboardView

urlpatterns = [
    path('teacher/add/', TeacherAddView.as_view(), name='teacher_add'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher_list'),
    path('', SignInView.as_view(), name='sign_in'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
