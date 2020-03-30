from django.shortcuts import render
from subjects.models import Subject

# Create your views here.


def subjects(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'subjects/subjects.html', context)
