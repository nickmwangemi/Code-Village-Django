from django.db import models
from account.models import Account

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    idNo = models.CharField(max_length=200)
    customerNo = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    pin = models.CharField(max_length=10)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_Customers'

    def __str__(self):
        return self.name
