from rest_framework import viewsets, filters

from api.restaurants.serializers import RestaurantSerializer
from apps.restaurants.models import Restaurant


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
