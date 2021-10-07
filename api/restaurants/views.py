from rest_framework import viewsets

from api.restaurants.serializers import RestaurantSerializer
from apps.restaurants.models import Restaurant


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
