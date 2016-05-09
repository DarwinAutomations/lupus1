'''
Created on 30 Aug 2015

@author: Simon Kindhauser
'''
import pygame, os
from multiprocessing.process import Process
from time import sleep

discon = False

class PscUserInputService(object):
    def __init__(self, accessLevel, eightApi):
        self.accessLevel = accessLevel
        self._eightApi = eightApi

        pygame.init()
        self.check()
        thread = Process(target=self.inputHandler)
        thread.start()
        
    def check(self):
        global discon
        try:
            pygame.joystick.quit()
            pygame.joystick.init()
            joystick_count = pygame.joystick.get_count()
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
            if not joystick_count: 
                if not discon:
                    os.system("./reconnect.sh")
                    discon = True
                sleep(0.5)
                self.check()
            else:
                discon = False
        except:
            self.check()

    def inputHandler(self):
        try:
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.JOYAXISMOTION:
                    # velocity
                        if event.axis == 13:
                            self.setVelocity(self.calculateVelocity(self.toPercent(event.value + 1)))
                        if event.axis == 15:
                            self.setVelocity(self.calculateVelocity(-self.toPercent(event.value + 1)))
                    # direction
                        if event.axis == 2:
                            self.setDirection(self.calculateDirection(self.toPercent((event.value * -1) + 1)))
                    # break
            self.check()        
            sleep(0.1)
        except KeyboardInterrupt:
            self.controller.quit()     

    def setVelocity(self, velocity):
        self._eightApi.setVelocity(self.accessLevel, int(velocity))
        self._eightApi.setVelocityAccessLevel(self.accessLevel, self.accessLevel)
    
    def calculateVelocity(self, velocity):
        currentVelocity = self._eightApi.getVelocity()
        if currentVelocity < velocity:
            return velocity
        if velocity < -5:
            return velocity
        return  currentVelocity
        
    def toPercent(self, value):
        return value * 50

    def setDirection(self, direction):
        self._eightApi.setDirection(self.accessLevel, int(direction))
        self._eightApi.setDirectionAccessLevel(self.accessLevel, self.accessLevel)
        
    def calculateDirection(self, value):
        return value
