'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''
from application.services.policies.VelocityPolicy import VelocityPolicy
from application.services.policies.DirectionPolicy import DirectionPolicy

class EightApi(object):
    '''
    The eight API is the interface used by all controlling components.
    It provides the functionality of the car in a simplified way.
    '''
    
    SUCCESS = True
    FAILED = False

    def __init__(self, steeringService):
        self.steeringService = steeringService
        
    def setVelocity(self, accessLevel, velocity):
        """
        Sets the velocity if the access level is allowed to do so and the velocity is legit.
        
        AccessLevel is the level of access of the accessor.
        Velocity is the requested velocity.
        
        Returns SUCCESS if operation was successful.
        Returns FAILED if operation had failed.
        """
        if VelocityPolicy.isAllowedToSet(accessLevel) and VelocityPolicy.isLegitVelocity(velocity):
            self.steeringService.setVelocity(velocity)
            return self.SUCCESS
        return self.FAILED

    def getVelocity(self):
        """
        Returns the value of the velocity in the steering service.
        
        Returns the current velocity.
        """
        
        return self.steeringService.getVelocity()

    def setVelocityAccessLevel(self, accessorAccessLevel, accessLevel):
        """
        Sets the lowest required access level for using velocity
        
        AccessorAccessLevel is the level of access of the accessor.
        AccessLevel is the level the access the operator wants it to be.
        """
        if VelocityPolicy.setAccessLevel(accessorAccessLevel, accessLevel) == VelocityPolicy.SUCCESS:
            return self.SUCCESS
        return self.FAILED
    
    def setDirection(self, accessLevel, direction):
        if DirectionPolicy.isAllowedToSet(accessLevel) and DirectionPolicy.isLegitDirection(direction):
            self.steeringService.setDirection(direction)
            return self.SUCCESS
        return self.FAILED
    
    def getDirection(self):
        return self.steeringService.getDirection()
    
    def setDirectionAccessLevel(self, accessorAccessLevel, accessLevel):
        if DirectionPolicy.setAccessLevel(accessorAccessLevel, accessLevel) == DirectionPolicy.SUCCESS:
            return self.SUCCESS
        return self.FAILED
