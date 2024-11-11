from django.db import models

from django.db import models

class Student(models.Model):
    index_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    average_grade = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.index_number})"
