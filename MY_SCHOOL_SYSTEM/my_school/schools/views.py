from django.shortcuts import render
from schools.models import School

# Create your views here.


def school_index(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)
