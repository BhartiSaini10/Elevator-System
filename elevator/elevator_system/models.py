from django.db import models

class ElevatorManager(models.Manager):
    pass

class Elevator(models.Model):
    floor = models.IntegerField(default=0)
    status = models.CharField(max_length=30, default="Active")
    door_status = models.CharField(max_length=30, default="closed")
    maintenance_due = models.BooleanField(default=False)
    last_maintenance = models.DateField(default="2022-11-01")
    capacity = models.IntegerField(default=10)
    current_direction = models.CharField(choices=[("up", "Up"), ("down", "Down"), ("idle", "Idle")], max_length=10, default="idle")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ElevatorManager()

    def __str__(self):
        return self.status


class ElevatorRequest(models.Model):
    objects = ElevatorManager()
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.elevator} - {self.floor}'


class Request(models.Model):
    objects = ElevatorManager()
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    direction = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Elevator {self.elevator.id} - Floor {self.floor} - Direction {self.direction}"






