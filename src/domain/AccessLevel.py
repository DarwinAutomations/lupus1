'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''
from multiprocessing import Value

class AccessLevel(object):
    '''
    The access level is used to validate if an actions source is authorised to do something.
    '''
    
    def __init__(self, accessLevel, accessorName):
        self.__AccessLevel = Value("i", accessLevel)
        self._AccessorName = accessorName
    
    def getAccessLevel(self):
        return self.__AccessLevel.value
    def setAccessLevel(self, value):
        self.__AccessLevel.value = value
    
    def getAccessorName(self):
        return self._AccessorName
    
    def isEquals(self, accessLevel):
        return self.getAccessLevel() == accessLevel.getAccessLevel()
    
    def isHigher(self, accessLevel):
        return self.getAccessLevel() < accessLevel.getAccessLevel()
    
    def isLower(self, accessLevel):
        return self.getAccessLevel() > accessLevel.getAccessLevel()
