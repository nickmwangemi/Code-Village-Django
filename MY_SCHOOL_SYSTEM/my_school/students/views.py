from django.shortcuts import render
from students.models import Student
from subjects.models import Subject

# Create your views here.


def student_index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students.html', context)

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    subject = Subject.objects.get(pk=pk)
    context = {
        "student": student,
        "subject": subject,
    }
    return render(request, "students/student_detail.html", context)

