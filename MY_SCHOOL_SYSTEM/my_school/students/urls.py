from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path("students/", views.student_index, name="student_index"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/add/", views.add, name="add"),

]
