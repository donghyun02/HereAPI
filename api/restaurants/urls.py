from django.urls import path
from rest_framework import routers

from api.restaurants.views import RestaurantViewSet, ReservationTimeView, ReservationView

app_name = 'restaurants'

router = routers.SimpleRouter()
router.register('restaurants', RestaurantViewSet)

urlpatterns = [
    path('reserved-times/', ReservationTimeView.as_view(), name='reserved-time'),
    path('reservations/', ReservationView.as_view(), name='reservation'),
]
urlpatterns += router.urls
