from django.db import models

from apps.user.models import User


# Create your models here.
class Ride(models.Model):
    id_ride = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=20, blank=True)
    pickup_latitude = models.FloatField(null=True)
    pickup_longitude = models.FloatField(null=True)
    dropoff_latitude = models.FloatField(null=True)
    dropoff_longitude = models.FloatField(null=True)
    pickup_time = models.DateTimeField(null=True)
    # foreign keys
    rider = models.ForeignKey(User, related_name="user_rider", on_delete=models.CASCADE, db_column="id_rider")
    driver = models.ForeignKey(User, related_name="user_driver", on_delete=models.CASCADE, db_column="id_driver")

    class Meta:
        db_table = "ride"
        verbose_name = "Ride"
        verbose_name_plural = "Rides"


class RideEvent(models.Model):
    id_ride_event = models.BigAutoField(primary_key=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, db_column="id_ride")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ride_event"
        verbose_name = "Ride Event"
        verbose_name_plural = "Ride Events"
