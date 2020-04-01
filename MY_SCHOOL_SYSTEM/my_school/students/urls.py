from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_index, name="students"),
    path("<int:pk>/", views.student_detail, name="student_detail"),

]
