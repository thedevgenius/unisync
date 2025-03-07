import json

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Fees
# Create your views here.
class FeesAddView(TemplateView):
    template_name = 'payment/fees_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fee = Fees.objects.get(id=3)
        # json_string = str(fee.data)
        if isinstance(fee.data, dict):  
            py_dict = fee.data  # Already a dictionary, no need to parse

        elif isinstance(fee.data, str):  
            try:
                py_dict = json.loads(fee.data)  # Convert JSON string to dictionary
            except json.JSONDecodeError:
                py_dict = {}  # Handle invalid JSON safely

        else:
            py_dict = {}  # Handle unexpected types

        print(py_dict) 
        return context
    