from datetime import datetime

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.restaurants.serializers import RestaurantSerializer, ReservationSerializer
from apps.restaurants.models import Restaurant, Reservation


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'address']
    filterset_fields = ['types__code']
    ordering = ['id']


class ReservationTimeView(APIView):
    def get(self, request):
        seat_id = request.query_params.get('seat_id')
        date = request.query_params.get('date')

        data = Reservation.objects.get_reserved_times(seat_id, date)

        return Response(data=data, status=status.HTTP_200_OK)


class ReservationView(APIView):
    def post(self, request):
        seat_id = request.data.get('seat_id')
        reserved_datetime = timezone.make_aware(
            datetime.strptime(
                request.data.get('datetime'),
                '%Y-%m-%d %H:%M:%S',
            )
        )
        name = request.data.get('name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        data = Reservation.objects.reserve(seat_id, reserved_datetime, name, email, phone_number)
        serializer = ReservationSerializer(data)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
