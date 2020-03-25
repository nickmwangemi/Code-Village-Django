from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    shortName = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_Currency'

    def __str__(self):
        return self.name
