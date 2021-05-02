from django.contrib import admin
from .models import Court, Access

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'booked', 'occupied', 'slug')

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('ip', 'access_time', 'court', 'play_time')
