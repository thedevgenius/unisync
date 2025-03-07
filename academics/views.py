from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from collections import defaultdict
from hashids import Hashids

from .models import Course
# Create your views here.

hashids = Hashids(salt='academics', min_length=10)


class CourseListView(ListView):
    template_name = 'academics/course_list.html'
    model = Course
    context_object_name = 'courses'

class CourseDetailView(TemplateView):
    template_name = 'academics/course_details.html'
    
    def get(self, request, *args, **kwargs):
        hash_id = kwargs.get('hash_id')
        course_id = hashids.decode(hash_id)[0]
        course = Course.objects.get(pk=course_id)
        return render(request, self.template_name, {'course': course})
    
    



    
    
    