from django.db import models

class Doors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    is_car_park = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description}"

class DoorRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    recorded_at = models.DateTimeField()
    recorded_date = models.CharField(max_length=30)
    recorded_time = models.CharField(max_length=30)
    doors = models.ForeignKey(Doors, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}"
