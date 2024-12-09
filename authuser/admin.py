from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from .models import Account



@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


# Register Account model with inline AccountInfo
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone','firstname','lastname', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('firstname','lastname','phone',)}),
    )



    
