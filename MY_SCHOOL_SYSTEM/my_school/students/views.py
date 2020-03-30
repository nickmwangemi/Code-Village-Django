from django.shortcuts import render
from students.models import Student
# Create your views here.


def student_index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students.html', context)
