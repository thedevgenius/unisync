from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from collections import defaultdict

from payment.models import Fees
from .models import Course

# from .forms import CourseAddForm

# # Create your views here.
class CourseListView(ListView):
    template_name = 'academics/course_list.html'
    model = Course
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    template_name = 'academics/course_details.html'
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fees = Fees.objects.filter(course=self.object, year__status=True).values('due_date', 'particular__name', 'amount')
        grouped_data = defaultdict(list)
        for fee in fees:
            grouped_data[fee['due_date']].append({'particular': fee['particular__name'], 'amount': fee['amount']})
        context['fees'] = dict(grouped_data)

        return context



    
    
    