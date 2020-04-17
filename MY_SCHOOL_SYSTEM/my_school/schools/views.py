from django.shortcuts import render,redirect
from schools.models import School
from students.models import Student

# Create your views here.


def school_index(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)


def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    # select * from students where school_id=x
    students = Student.objects.filter(school_id=pk)
    context = {
        "school": school,
        "students": students,
    }
    return render(request, "schools/school_detail.html", context)



def add(request):
    if request.method == "POST":
        form = request.POST
        # print(form) # for testing
        school = School()
        school.name = form['name']
        school.code = form['code']
        school.address = form['address']
        school.no_of_students = form['no_of_students']
        school.save()

        return redirect('schools:school_detail',school.pk)
    
    context = {}

    return render(request, 'schools/add.html',context)