from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('accountNumber', 'currency', 'balance',)
    search_fields = ('accountNumber', 'currency__name',
                     'currency__code', 'currency__shortName')


# Register your models here.
admin.site.register(Account, AccountAdmin)
