from django.contrib import admin
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'address', 'no_of_students')
    search_fields = ('name', 'code', 'address', 'no_of_students')


# Register your models here.
admin.site.register(School, SchoolAdmin)
