from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User



class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username']


admin.site.register(User, UserAdmin)


