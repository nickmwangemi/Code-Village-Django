from django.contrib import admin
from currency.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'shortName')
    search_fields = ('name', 'code', 'shortName')


# allow display on admin page
admin.site.register(Currency, CurrencyAdmin)
