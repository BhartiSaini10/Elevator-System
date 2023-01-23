from .views import ElevatorViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ElevatorRequestViewSet
from .views import next_destination
from .views import current_direction

router = DefaultRouter()
router.register(r'requests', ElevatorRequestViewSet)

urlpatterns = [
    path('elevator/<int:elevator_pk>/current_direction/', current_direction, name='current_direction'),
    path('elevator/<int:elevator_pk>/next_destination/', next_destination, name='next_destination'),
    path('init/', ElevatorViewSet.as_view({'post': 'create'}), name='init'),
    path('elevator/<int:elevator_pk>/requests/', ElevatorRequestViewSet.as_view({'get': 'list'}), name='requests'),
    *router.urls
]