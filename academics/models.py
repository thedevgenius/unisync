from django.db import models
from hashids import Hashids

# Create your models here.

hashids = Hashids(salt='academics', min_length=10)

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('Diploma', 'Diploma'),
        ('PhD', 'Doctorate'),
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    eligibility = models.TextField(null=True, blank=True)
    max_year = models.IntegerField(verbose_name='Duration Year')
    max_month = models.IntegerField(verbose_name='Duration Month', null=True, blank=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='UG')
    
    
    def __str__(self):
        return self.name
    
    def get_hash_id(self):
        return hashids.encode(self.id)
    

class AcademicYear(models.Model):
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.start.year} - {self.end.year}'