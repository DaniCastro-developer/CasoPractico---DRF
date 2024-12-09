from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ReservationViewSet

router = DefaultRouter()

router.register(r'room', RoomViewSet, basename='room')

urlpatterns = router.urls