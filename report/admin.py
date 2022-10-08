from django.contrib import admin
from .models import Doors, DoorRecord


class DoorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'is_car_park')

class DoorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'recorded_at', 'doors', 'count')

admin.site.register(Doors, DoorsAdmin)
admin.site.register(DoorRecord, DoorRecordAdmin)
