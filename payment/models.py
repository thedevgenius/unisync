from django.db import models


# Create your models here.
class Particular(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class Fees(models.Model):
    year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    particular = models.ForeignKey(Particular, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.particular.name} - {self.due_date}"
    
    class Meta:
        ordering = ['due_date']
        unique_together = ('due_date','particular', 'course', 'year')
