from rest_framework import serializers

from apps.restaurants.models import Restaurant, Seat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'id',
            'name',
            'image',
            'description',
        )


class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        source='get_rating',
        max_digits=3,
        decimal_places=2,
        coerce_to_string=False,
    )
    seats = SeatSerializer(
        many=True,
    )

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'name',
            'image',
            'address',
            'rating',
            'seats',
        )
