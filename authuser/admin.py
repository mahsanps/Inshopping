from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from store.models import AccountInfo
from .models import Account



@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass

# Inline admin for AccountInfo within AccountAdmin
class AccountInfoInline(admin.StackedInline):
    model = AccountInfo
    extra = 0

# Register Account model with inline AccountInfo
@admin.register(Account)
class AccountAdmin(UserAdmin):
    inlines = [AccountInfoInline]
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )
# Corrected AccountInfoAdmin
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = [
        'firstname',
        'lastname',
      
    ]

admin.site.register(AccountInfo, AccountInfoAdmin)  
    
