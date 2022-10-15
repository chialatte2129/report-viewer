from django.contrib import admin
from .models import Door, DoorAction, DoorRecord, Area

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class DoorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area', 'is_car_park')

class DoorActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'door', 'description', 'action')

class DoorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'recorded_at', 'door_action', 'count')

admin.site.register(Door, DoorsAdmin)
admin.site.register(DoorAction, DoorActionAdmin)
admin.site.register(DoorRecord, DoorRecordAdmin)
admin.site.register(Area, AreaAdmin)