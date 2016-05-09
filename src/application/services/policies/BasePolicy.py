'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''

class BasePolicy(object):
    '''
    The velocity polices class provides all policies related to velocity.
    '''
    SUCCESS = True
    FAILED = False
    
    __currentAccessesLevel = None

    def __init__(self):
        pass
        
    @staticmethod
    def isAllowedToSet(accessLevel):
        return not BasePolicy.__currentAccessesLevel.isHigher(accessLevel)
    
    @staticmethod
    def setAccessLevel(accessorAccessLevel, accessLevel):
        if BasePolicy.isAllowedToSet(accessorAccessLevel):
            BasePolicy.__currentAccessesLevel.setAccessLevel(accessLevel.getAccessLevel())
            return BasePolicy.SUCCESS
        return BasePolicy.FAILED 
