# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_lastname', 'student_firstname', 'student_gender', 'student_yearlevel', 'student_course', 'student_email', 'student_units', 'student_birthdate']
