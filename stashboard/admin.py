from django.contrib import admin
from stashboard.models import Service, Region, Status, Announcement, Issue, Update

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'region', 'status']
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['name', 'region', 'description']

class AnnouncementAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(Region)
admin.site.register(Status)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Issue)
admin.site.register(Update)

