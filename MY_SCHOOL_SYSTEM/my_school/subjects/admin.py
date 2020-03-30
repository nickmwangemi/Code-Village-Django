from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'student')
    search_fields = ('name', 'score', 'student__name')


# Register your models here.
admin.site.register(Subject, SubjectAdmin)
