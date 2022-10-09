from django.contrib import admin
from .models import Door, DoorRecord


class DoorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'is_car_park')

class DoorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'recorded_at', 'doors', 'count')

admin.site.register(Door, DoorsAdmin)
admin.site.register(DoorRecord, DoorRecordAdmin)
