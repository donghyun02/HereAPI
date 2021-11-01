from django.contrib import admin

from apps.restaurants.models import Restaurant, Review, Seat, RestaurantCarousel


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantCarousel)
class RestaurantCarouselAdmin(admin.ModelAdmin):
    pass