from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('course/list/', CourseListView.as_view(), name='course_list'),
    path('course/<str:hash_id>/', CourseDetailView.as_view(), name='course_details'),
]


