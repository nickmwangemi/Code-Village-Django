from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path("subjects/", views.subjects, name="subjects"),
    path("subjects/<int:pk>/", views.subject_detail, name="subject_detail"),
    path("subjects/add/", views.add, name="add"),

]
