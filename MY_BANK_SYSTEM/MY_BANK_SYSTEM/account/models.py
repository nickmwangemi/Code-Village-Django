from django.db import models
from currency.models import Currency

# Create your models here.


class Account(models.Model):
    accountNumber = models.CharField(max_length=200)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.FloatField()

    class Meta:
        db_table = 'tbl_Account'

    def __str__(self):
        return self.accountNumber
