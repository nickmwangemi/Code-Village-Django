from django.shortcuts import render
from schools.models import School

# Create your views here.


def dashboard(request):
    schools = School.objects.all()

    context = {
        'schools':schools,
    }
    return render(request, 'dashboard/dashboard.html', context)
