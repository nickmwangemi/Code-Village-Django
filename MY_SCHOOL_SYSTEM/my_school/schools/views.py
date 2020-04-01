from django.shortcuts import render
from schools.models import School
from students.models import Student

# Create your views here.


def school_index(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)


# def school_detail(request, school_id):
#     school = School.objects.get(pk=school_id)
#     # student = Student.objects.filter(pk=student_id)

#     context = {
#         'school': school,

#     }
#     return render(request, 'schools/school_detail.html', context)


# def student_detail(request):
#     students = Student.objects.all()

#     context = {
#         'students': students,

#     }
#     return render(request, 'schools/school_detail.html', context)

def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    students = Student.objects.all()
    context = {
        "school": school,
        "students": students,
    }


    return render(request, "schools/school_detail.html", context)