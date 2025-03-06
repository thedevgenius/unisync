from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class FeesAddView(TemplateView):
    template_name = 'payment/fees_add.html'