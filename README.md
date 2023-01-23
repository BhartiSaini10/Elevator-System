#  PROBLEM STATEMENT - Elevator-System
  An elevator system, which can be initialised with N elevators and maintains the elevator states as well.
A. Each elevator has below capabilities:
  Move Up and Down
  Open and Close Door
  Start and Stop Running
  Display Current Status
  Decide whether to move up or down, based on a list of requests from users.

B. Elevator System takes care of:
  Decides which lift to associate which floor.
  Marks which elevator is available or busy.
  Can mark which elevator is operational and which is not.

C. Assumptions:
  Number of elevators in the system will be defined by the API to intialise the elevator system
  Elevator System has got only one button per floor.
  So if there are a total of 5 floors, there will be 5 buttons per floor.
  Note that, this doesn't not mimic real world, when you would have a total of 10 buttons for 5 floors ( one for up and one for down)
  Once the elevator reaches its called point, then based on what floor is requested, it moves either up or down.
  Assume the API calls which make the elevator go up/down or stop will reflect immediately. When the API to go up is called, you can assume that the elevator has already reached the above floor. 
  The system has to assign the most optimal elevator to the user according to their request.

D. API’s required:
Initialise the elevator system to create ‘n’ elevators in the system
Fetch all requests for a given elevator
Fetch the next destination floor for a given elevator
Fetch if the elevator is moving up or down currently
Saves user request to the list of requests for a elevator
Mark a elevator as not working or in maintenance 
Open/close the door.



#  CODE SUMMARY :

ElevatorViewSet is a subclass of viewsets.ModelViewSet, which is a generic view that provides CRUD functionality for a model. It sets the queryset to all the elevators in the system and the serializer class to ElevatorSerializer. The create method is overridden in order to allow for creating multiple elevators at once.

ElevatorRequestViewSet is also a subclass of viewsets.ModelViewSet, it provides CRUD functionality for the ElevatorRequest model. The list method is overridden to allow for filtering the queryset by elevator primary key.

next_destination, current_direction, CreateRequestView, UpdateElevatorStatusView, UpdateElevatorDoorView are different views, each one is designed to handle specific functionality such as getting the next destination floor for a given elevator, getting the current direction of the elevator, creating a request, updating the status of the elevator, updating the door status of the elevator respectively.


