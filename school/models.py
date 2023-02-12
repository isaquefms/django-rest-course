from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    document = models.CharField(max_length=9)
    document_number = models.CharField(max_length=11)
    born_date = models.DateField()

    def __str__(self):
        return self.first_name
    

class Course(models.Model):
    class CourseLevel(models.TextChoices):
        BASIC = 'B', 'Basic'
        INTERMEDIATE = 'I', 'Intermediate'
        ADVANCED = 'A', 'Advanced'

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=CourseLevel.choices, default=CourseLevel.BASIC)

    def __str__(self):
        return f'{self.code} - {self.name}'
