from django.urls import path
from . import views

urlpatterns = [
    path("", views.school_index, name="schools"),
    path("<int:pk>/", views.school_detail, name="school_detail"),
   

]
