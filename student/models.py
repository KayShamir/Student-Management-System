from django.db import models

# Create your models here.
class Student(models.Model):
    student_lastname = models.CharField(max_length=50)
    student_firstname = models.CharField(max_length=50)
    student_gender = models.CharField(max_length=10)
    student_yearlevel = models.IntegerField()
    student_course = models.CharField(max_length=255)
    student_email = models.EmailField()
    student_units = models.IntegerField()
    student_birthdate = models.DateField()

    def __str__(self):
        return self.student_lastname