from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'idNo', 'customerNo',
                    'phoneNumber', 'pin', 'account')
    search_fields = ('name', 'idNo')


# allow display on admin page
admin.site.register(Customer, CustomerAdmin)
