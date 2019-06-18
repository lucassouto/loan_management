from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User


class LoanManagementUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class LoanManagementUserAdmin(UserAdmin):
    form = LoanManagementUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        ('Extra fields', {'fields': ('id_external', 'name', 'registry_code', 'phone')}),
    )


admin.site.register(User, LoanManagementUserAdmin)
