from django.contrib import admin
from registration_app.models import Account, ApplicantRegister, CircularRegister, AddCircular
from registration_app.forms import ApplicantRegisterForm, AccountForm, AddCircularForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    add_form = AccountForm
    # form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'is_staff',) 
    list_filter = ('email', 'is_staff',) 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',  'is_superuser', 'groups', 'user_permissions',)}),   #'is_customer' , 'is_seller'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Account, AccountAdmin)

admin.site.register(ApplicantRegister)
admin.site.register(CircularRegister)
admin.site.register(AddCircular)