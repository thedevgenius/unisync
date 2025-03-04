from django.urls import path
from .views import TeacherAddView

urlpatterns = [
    path('teacher/add/', TeacherAddView.as_view(), name='teacher_add'),
    # path('college/list/', CollegeListView.as_view(), name='college_list'),
]
