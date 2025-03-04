from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    eligibility = models.TextField(null=True, blank=True)
    max_year = models.IntegerField(verbose_name='Duration Year')
    max_month = models.IntegerField(verbose_name='Duration Month', null=True, blank=True)
    
    def __str__(self):
        return self.name