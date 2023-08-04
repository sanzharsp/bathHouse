from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin

class Users_Admin(UserAdmin):
    model = User
    list_display = ('phone_number', 'first_name', 'is_superuser','is_staff')
    list_filter = ('phone_number', 'first_name','is_superuser',)
    fieldsets = (
        (None, {'fields': ('password', 'first_name','phone_number',)}),
        ('Права доступа и потверждение', {'fields': ('is_staff','is_superuser')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'first_name',)},
            
        ),
         ('Права доступа и потверждение', {'fields': ('is_staff','is_superuser')}),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)


class BathHouseModelAdmin(admin.ModelAdmin):
    model = BathHouseModel
    list_display = ('number_key', 'first_name', 'number_phone', 'date_start', 'my_type')
    list_filter = ('number_key', 'first_name', 'number_phone','date_start', 'my_type' )
    search_fields = ('number_key',)
    ordering = ('number_key',)

admin.site.register(User,Users_Admin)
admin.site.register(BathHouseModel,BathHouseModelAdmin)