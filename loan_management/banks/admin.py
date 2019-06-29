from django.contrib import admin

from .models import Bank


class BankAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bank, BankAdmin)
