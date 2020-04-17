from django.shortcuts import render,redirect
from students.models import Student
from subjects.models import Subject
from schools.models import School

# Create your views here.


def student_index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students.html', context)

def student_detail(request, pk):
    # select from students where student_id=x
    student = Student.objects.get(pk=pk)
    # select * from subjects where student_id = pk
    subjects = Subject.objects.filter(student_id=pk)
    

    # def getGrade(score):
    #     if score >= 80 and score <= 100:
    #         return 'A'
    #     elif score >= 60 and score < 80:
    #         return 'B'
    #     elif score >= 40 and score < 60:
    #         return 'C'
    #     elif score >= 0 and score < 40:
    #         return 'D'
    #     else:
    #         'Unknown Grade'
    
    # # grade = getGrade(score)

    context = {
        'student': student,
        'subjects':subjects,
        # 'grade':grade
    }
    return render(request, 'students/student_detail.html', context)


def add(request):
    if request.method == "POST":
        form = request.POST
        student = Student()
        student.name = form['name']
        student.registration_number = form['registration_number']
        student.address = form['address']
        student.age = form['age']
        #1
        student.school = School.objects.get(pk=form['school'])
        student.save()

        return redirect('students:student_detail',student.pk)
    
    

    schools = School.objects.all()
    context = {'schools': schools}

    return render(request, 'students/addStudent.html',context)
