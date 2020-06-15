# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle():
    '''This is the base class.'''
    pass

class FlightVehicle(Vehicle):
    '''This is Child class from the parent vehicle'''
    pass

class Starship(FlightVehicle):
    ''' This is grandChild from the base class'''
    pass

class Airplane(FlightVehicle):
    ''' This class inherits from the subclass FlightVehicle'''
    pass


class GroundVehicle(Vehicle):
    ''' This is the child from the vehicle class'''
    pass


class Car(GroundVehicle):
    '''This class inherits from GroundVehicle'''
    pass


class Motorcycle(GroundVehicle):
    '''This class inherits from GroundVehicle'''
    pass
