from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.TextField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    no_of_students = models.IntegerField(null=True)

    class Meta:
        db_table = 'tbl_schools'

    def __str__(self):
        return self.name
