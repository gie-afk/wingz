from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication

from rest_framework.pagination import PageNumberPagination

from apps.ride.models import Ride
from .serializers import RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = PageNumberPagination
    filterset_fields = {
        "status": ["exact"],
        "rider__email": ["exact"],
    }
    ordering_fields = ["pickup_time"]
