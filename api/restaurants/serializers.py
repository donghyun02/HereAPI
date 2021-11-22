from rest_framework import serializers

from apps.restaurants.models import Restaurant, Seat, RestaurantCarousel, Type, Reservation


class RestaurantWithoutSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'name',
        )


class SeatSerializer(serializers.ModelSerializer):
    restaurant = RestaurantWithoutSeatSerializer()

    class Meta:
        model = Seat
        fields = (
            'id',
            'name',
            'image',
            'description',
            'restaurant',
        )


class RestaurantCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCarousel
        fields = (
            'id',
            'image',
        )


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'name',
            'code',
        )


class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        source='get_rating',
        max_digits=3,
        decimal_places=2,
        coerce_to_string=False,
    )
    carousel = RestaurantCarouselSerializer(
        many=True,
    )
    seats = SeatSerializer(
        many=True,
    )
    types = TypeSerializer(
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
            'carousel',
            'seats',
            'types',
        )


class ReservationSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()

    class Meta:
        model = Reservation
        fields = (
            'id',
            'seat',
            'reserved_datetime',
            'booker_name',
            'booker_email',
            'booker_phone_number',
        )
