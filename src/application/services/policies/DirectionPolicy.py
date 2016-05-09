'''
Created on 14 Nov 2015

@author: samantha
'''
from application.services.policies.BasePolicy import BasePolicy

class DirectionPolicy(BasePolicy):
    '''
    The direction policy provides all policies related to direction.
    '''
                    
    @staticmethod
    def isLegitDirection(direction):
        try:
            if direction > 100 or direction < -100:
                return False
            else:
                return True
        except:
            return False
