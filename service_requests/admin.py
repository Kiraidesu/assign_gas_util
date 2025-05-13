from django.contrib import admin

from .models import ServiceRequest

# Register your models here.

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'request_type', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'request_type')
    search_fields = ('description',)
    