from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Particular, Fees
from academics.models import Course
# Create your views here.
# class FeesAddView(TemplateView):
#     template_name = 'pay/fees_add.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['particulars'] = Particular.objects.all()
#         context['years'] = AcademicYear.objects.all()
#         context['courses'] = Course.objects.all()
#         return context
    
#     def post(self, request, *args, **kwargs):
#         data = request.POST
#         particulars = Particular.objects.all()
#         value = {}
#         for part in particulars:
#             if data.get(f'part_{part.id}'):
#                 value[part.id] = int(data.get(f'part_{part.id}'))
#         Fees.objects.create(
#             title=data.get('title'),
#             year_id=data.get('year'),
#             course_id=data.get('course'),
#             due_date=data.get('due_date'),
#             data=value,
#         )
#         return render(request, self.template_name, self.get_context_data())
    
# class FeesEditView(TemplateView):
#     template_name = 'pay/fees_edit.html'

#     def get(self, request, **kwargs):
#         id = kwargs['id']
#         fee = Fees.objects.get(id=id)
#         particulars = Particular.objects.all()
#         years = AcademicYear.objects.all()
#         courses = Course.objects.all()
        
#         return render(request, self.template_name, {
#             'fee': fee,
#             'particulars': particulars,
#             'years': years,
#             'courses': courses,
#         })
