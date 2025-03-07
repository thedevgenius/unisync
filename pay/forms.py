from django import forms

# class FeesAddForm(forms.Form):
#     year = forms.CharField(max_length=15)
#     course = forms.CharField(max_length=10)
#     due_date = forms.DateField()
#     data = forms.JSONField()
    
#     def __str__(self):
#         return f'{self.course} - {self.year}'
    
#     class Meta:
#         unique_together = ['year', 'course', 'due_date']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         year = cleaned_data.get('year')
#         course = cleaned_data.get('course')
#         due_date = cleaned_data.get('due_date')
#         data = cleaned_data.get('data')
        
#         if not year or not course or not due_date or not data:
#             raise forms.ValidationError('All fields are required')
        
#         return cleaned_data