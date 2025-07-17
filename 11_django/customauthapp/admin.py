from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'phone_number', 'role']
    search_fields = ['email', 'name', 'phone_number']
    ordering = ['email']
    list_editable = ['role']