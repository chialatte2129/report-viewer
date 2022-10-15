from django.db import models

class Area(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"

class Door(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    is_car_park = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_options(self):
        doors = Door.objects.all().values("id", "name")
        return [[door["id"], door["name"]] for door in doors ]

class DoorAction(models.Model):
    CHOICES = (
        ('in', 'IN'),
        ('out', 'OUT'),
    )
    id = models.BigIntegerField(primary_key=True)
    door = models.ForeignKey(Door, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100)
    action = models.CharField(max_length=10, default="in", null=True, choices=CHOICES)

    def __str__(self):
        return f"{self.description}"
    
    @classmethod
    def get_map(self):
        doors = DoorAction.objects.all().values("id", "description")
        return { door["description"]:door["id"] for door in doors}
    
    @classmethod
    def get_options(self):
        doors = DoorAction.objects.all().values("id", "description")
        return [[door["id"], door["description"]] for door in doors ]

class DoorRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    recorded_at = models.DateTimeField()
    recorded_date = models.CharField(max_length=30)
    recorded_time = models.CharField(max_length=30)
    door_action = models.ForeignKey(DoorAction, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}"
