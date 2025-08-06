from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, map_view

router = DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),      # e.g., /api/places/
    path('map/', map_view, name="map"),  # e.g., /map/
]
