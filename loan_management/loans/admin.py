from django.contrib import admin

from .models import Contract, Payment


class ContractAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contract, ContractAdmin)
admin.site.register(Payment, PaymentAdmin)
