'''
Created on 30 Aug 2015

@author: Simon Kindhauser
'''
from application.services.policies.VelocityPolicy import VelocityPolicy
from multiprocessing.process import Process
from multiprocessing import Value
from time import sleep
from ..libraries.MotorHAT import MotorHAT # does not work.
from application.services.policies.DirectionPolicy import DirectionPolicy

class SteeringService(object):
    '''
    This service provides direct and unconditional access to the steering hardware.
    '''
    
    def __init__(self):
        self.__actualSpeed = Value('f', 0.0)
        self._targetSpeed = Value('f', 0.0)
        
        self.__actualDirection = Value('f', 0.0)
        self._targetDirection = Value('f', 0.0)
    
        self.__setupMotors()
        
        steering = Process(target=self.steer)
        #steering.daemon = True
        steering.start()
    
    def __setupMotors(self):
        self.__motorShield = MotorHAT(0x60, 500)
        self.__servoShield = MotorHAT(0x40, 60)
        
        self.__motors = self.__motorShield.motors
        
        self.__servos = self.__servoShield.servos

    def steer(self):
        try:
            while True:
                self.__updateVelocity()
                self.__updateDirection()
                sleep(0.1)
        except KeyboardInterrupt:
            for motor in self.__motors:
                motor.run(MotorHAT.RELEASE)
  
# velocity
    def setVelocity(self, velocity):
        if VelocityPolicy.isLegitVelocity(velocity):
            self._targetSpeed.value = velocity
    
    def getVelocity(self):
        return self.__actualSpeed.value

    def __updateVelocity(self):
        self.__updateActualVelocity()
        print(self.getVelocity())
        velocity = int(self.getVelocity()*2.5)
        if velocity == 0:
            for motor in self.__motors:
                motor.run(MotorHAT.RELEASE)
            return
        elif velocity > 0:
            for motor in self.__motors:
                motor.run(MotorHAT.FORWARD)
        elif velocity < 0:
            for motor in self.__motors:
                motor.run(MotorHAT.BACKWARD)
        for motor in self.__motors:
                motor.setSpeed(abs(velocity))

    def __updateActualVelocity(self):
        self.__actualSpeed.value = self._targetSpeed.value
        #self._targetSpeed.value -= self._targetSpeed.value/10

#direction
    def setDirection(self, direction):
        if DirectionPolicy.isLegitDirection(direction):
            self._targetDirection.value = direction
    
    def getDirection(self):
        return self.__actualDirection.value

    def __updateDirection(self):
        self.__updateActualDirection()
        direction = int(self.getDirection()*0.09)+19
        for servo in self.__servos:
            servo.setDirection(direction)
    
    def __updateActualDirection(self):
        self.__actualDirection.value = self._targetDirection.value
        #self._targetSpeed.value -= self._targetSpeed.value/10

    
