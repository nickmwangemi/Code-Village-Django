from django.shortcuts import render, redirect
from subjects.models import Subject
from students.models import Student

# Create your views here.


def subjects(request):
    subjects = Subject.objects.all()
    # grade = Subject.getGrade(self=subjects)
    context = {
        'subjects': subjects,
        # 'grade':grade
    }
    return render(request, 'subjects/subjects.html', context)

def subject_detail(request, pk):
    student = Student.objects.filter(pk=pk)
    subject = Subject.objects.get(pk=pk)

    # evaluate grade
    
    context = {
        'subject':subject,
        'student':student
    }
    return render(request, 'subjects/subject_detail.html', context)

def add(request):
    if request.method == "POST":
        form = request.POST
        subject = Subject()
        subject.name = form['name']
        subject.score = form['score']
        subject.student = Student.objects.get(pk=form['student'])
        subject.save()

        return redirect('subjects:subject_detail',subject.pk)
    
    students = Student.objects.all()
    context = {
        'students':students,
        'subjects':subjects
    }

    return render(request, 'subjects/addSubject.html',context)


