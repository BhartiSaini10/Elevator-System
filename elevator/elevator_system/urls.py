from .views import ElevatorViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ElevatorRequestViewSet
from .views import next_destination
from .views import current_direction
from .views import CreateRequestView
from .views import UpdateElevatorStatusView

router = DefaultRouter()
router.register(r'requests', ElevatorRequestViewSet)

urlpatterns = [
    path('elevator/<int:pk>/status/', UpdateElevatorStatusView.as_view(), name='update_status'),
    path('elevator/<int:elevator_pk>/request/', CreateRequestView.as_view(), name='create_request'),
    path('elevator/<int:elevator_pk>/current_direction/', current_direction, name='current_direction'),
    path('elevator/<int:elevator_pk>/next_destination/', next_destination, name='next_destination'),
    path('init/', ElevatorViewSet.as_view({'post': 'create'}), name='init'),
    path('elevator/<int:elevator_pk>/requests/', ElevatorRequestViewSet.as_view({'get': 'list'}), name='requests'),
    *router.urls
]