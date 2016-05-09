'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''
from application.services.creators.AccessLevelBuilder import AccessLevelBuilder
from time import sleep
from multiprocessing.process import Process

class TestInputService(object):

    def __init__(self, accessLevel, eightApi):
        self.accessLevel = accessLevel
        self._eightApi = eightApi
        
    def start(self):
        print("starting test")
        testing = Process(target=self.test)
        #testing.daemon = True
        testing.start()
    
    def test(self):
        print("test started")
        for speed in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, speed))
            sleep(0.1)
        
        for i in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, 100))
            sleep(0.1);
        
        
        for speed in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, 100-speed))
            sleep(0.1);
            
            
        for speed in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, -speed))
            sleep(0.1)
        
        for i in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, -100))
            sleep(0.1);
        
        
        for speed in range(101):
            print(self._eightApi.setVelocity(self.accessLevel, -100+speed))
            sleep(0.1);
        
        
        self._eightApi.setVelocity(self.accessLevel, 0);
        self._eightApi.setVelocityAccessLevel(self.accessLevel, AccessLevelBuilder.createNullAccessLevel(""))
