from django import forms

# from .models import Course, Department

# class CourseAddForm(forms.ModelForm):
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. B. Tech'}))
#     code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. BTCS'}))
#     department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'select'}))
#     max_year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'e.g. 4'}))
#     max_month = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'e.g. 6'}))
#     class Meta:
#         model = Course
#         fields = '__all__'

    
