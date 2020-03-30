from django.urls import path
from . import views

urlpatterns = [
    path("", views.school_index, name="schools"),

]
