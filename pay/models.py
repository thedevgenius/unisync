from django.db import models

from academics.models import AcademicYear, Course
# Create your models here.
class Particular(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fees(models.Model):
    SLOT_CHOICES = [
        ('1', 'Pay 1'),
        ('2', 'Pay 2'),
        ('3', 'Pay 3'),
        ('4', 'Pay 4'),
        ('5', 'Pay 5'),
        ('6', 'Pay 6'),
    ]
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    slot = models.CharField(max_length=2, choices=SLOT_CHOICES)
    due_date = models.DateField()
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee = models.JSONField()

    def __str__(self):
        return f'{self.course.name} - {self.slot}'

    





