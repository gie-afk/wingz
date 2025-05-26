from rest_framework import serializers

from apps.ride.models import Ride, RideEvent
from apps.user.api.serializers import UserSerializer


class RideSerializer(serializers.ModelSerializer):
    rider = UserSerializer()
    driver = UserSerializer()

    class Meta:
        model = Ride
        fields = "__all__"


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = "__all__"
