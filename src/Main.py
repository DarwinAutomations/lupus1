'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''

from time import sleep

from application.services.EightApi import EightApi 
from infrastructures.SteeringService import SteeringService
from application.services.TestInputService import TestInputService
from infrastructures.PscUserInputService import PscUserInputService
from application.services.creators.AccessLevelBuilder import AccessLevelBuilder

if __name__ == '__main__':

    steeringService = SteeringService()
    eightApi = EightApi(steeringService)
    """
    pscRootInputService = PSControllerRootInputService(
            AccessLevelBuilder.createRootAccessLevel("root input process"),
            eightApi)
    
    TasService = TasService(
            AccessLevelBuilder.createSuperUserAccessLevel("root input process"),
            eightApi)
    """
    pscUserInputService = PscUserInputService(
            AccessLevelBuilder.createUserAccessLevel("user input process"), 
            eightApi)
    """
    testInputService = TestInputService(
            AccessLevelBuilder.createNullAccessLevel("Automated testing process"), 
            eightApi)
    testInputService.start()
    """
