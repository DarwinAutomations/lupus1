'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''

from domain.AccessLevel import AccessLevel

class AccessLevelBuilder(object):
    '''
    This supports the building of access levels.
    '''

    @staticmethod
    def createRootAccessLevel(accessorName):
        return AccessLevel(0, accessorName)
    
    @staticmethod
    def createSuperUserAccessLevel(accessorName):
        return AccessLevel(1, accessorName)
    
    @staticmethod
    def createUserAccessLevel(accessorName):
        return AccessLevel(2, accessorName)
    
    @staticmethod
    def createNullAccessLevel(accessorName):
        return AccessLevel(3, accessorName)
