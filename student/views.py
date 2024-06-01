from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import StudentForm
from .models import Student

def index(request):
    search_query = request.GET.get("search", "")
    course_filter = request.GET.get("course", "")  # Get the course filter parameter
    if search_query:
        students = Student.objects.filter(
            Q(id__icontains=search_query)  # Assuming 'id' is the primary key
            | Q(student_firstname__icontains=search_query)
            | Q(student_lastname__icontains=search_query)
            | Q(student_email__icontains=search_query)
        )
    elif course_filter:  # Check if course filter is applied
        students = Student.objects.filter(student_course=course_filter)
    else:
        students = Student.objects.all()

    form = StudentForm()
    return render(request, 'index.html', {'form': form, 'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')  # Redirect to index in case of a GET request or form invalid
