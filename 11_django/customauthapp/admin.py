from django.contrib import admin
from .models import CustomUser, Contact
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'phone_number', 'role']
    search_fields = ['email', 'name', 'phone_number']
    ordering = ['email']
    list_editable = ['role']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['created_at']