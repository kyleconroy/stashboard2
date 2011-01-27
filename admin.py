from django.contrib import admin
from stashboard.models import Service, Region, Status

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'region', 'status']
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['name', 'region', 'description']

admin.site.register(Service, ServiceAdmin)
