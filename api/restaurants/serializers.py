from rest_framework import serializers

from apps.restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        source='get_rating',
        max_digits=3,
        decimal_places=2,
        coerce_to_string=False,
    )

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'name',
            'image',
            'address',
            'rating',
        )
