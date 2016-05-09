'''
Created on 29 Aug 2015

@author: Simon Kindhauser
'''

from application.services.policies.BasePolicy import BasePolicy

class VelocityPolicy(BasePolicy):
    '''
    The velocity polices class provides all policies related to velocity.
    '''
                        
    @staticmethod
    def isLegitVelocity(velocity):
        try:
            if velocity > 100 or velocity < -100:
                return False
            else:
                return True
        except:
            return False
