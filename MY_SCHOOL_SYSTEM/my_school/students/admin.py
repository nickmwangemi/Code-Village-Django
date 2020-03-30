from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'address', 'age', 'school')
    search_fields = ('name', 'registration_number',
                     'address', 'age', 'school__name')


# Register your models here.
admin.site.register(Student, StudentAdmin)
