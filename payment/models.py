from django.db import models


# Create your models here.
class Particular(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class Fees(models.Model):
    year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)
    due_date = models.DateField()
    data = models.JSONField(default=None)
    
    def __str__(self):
        return f"{self.year.title} - {self.due_date}"
    
    class Meta:
        ordering = ['due_date']
        unique_together = ('due_date', 'course', 'year')
