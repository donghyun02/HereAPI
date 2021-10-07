from rest_framework import routers

from api.restaurants.views import RestaurantViewSet

router = routers.SimpleRouter()
router.register('restaurants', RestaurantViewSet)
urlpatterns = router.urls
