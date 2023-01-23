from rest_framework import viewsets
from .serializers import ElevatorSerializer
from .models import ElevatorRequest
from .serializers import ElevatorRequestSerializer
from django.shortcuts import get_object_or_404
from .models import Elevator
from django.http import JsonResponse

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def create(self, request, *args, **kwargs):
        n_elevators = request.data.get('n_elevators', 1)
        for i in range(n_elevators):
            Elevator.objects.create()
        return super().create(request, *args, **kwargs)

class ElevatorRequestViewSet(viewsets.ModelViewSet):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer

    def list(self, request, *args, **kwargs):
        elevator_pk = request.query_params.get('elevator_pk')
        if elevator_pk:
            self.queryset = self.queryset.filter(elevator__pk=elevator_pk)
        return super().list(request, *args, **kwargs)


def next_destination(request, elevator_pk):
    elevator = get_object_or_404(Elevator, pk=elevator_pk)
    next_request = elevator.elevatorrequest_set.order_by('request_time').first()
    resp = {'next_destination': next_request.floor} if next_request else {'next_destination': None}
    return JsonResponse(resp)


def current_direction(request, elevator_pk):
    elevator = get_object_or_404(Elevator, pk=elevator_pk)
    return JsonResponse({'current_direction': elevator.current_direction})

