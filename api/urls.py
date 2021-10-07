from django.urls import path, include

urlpatterns = [
    path('', include('api.restaurants.urls')),
]
