from atm_consts import *

class ATMOSPHERE:
    """
    This class will contain model of the atmosphere according to GOST - 4401-81
    """
    def get_AccelOfGravity(self, Height):
        """
        Function for calculating the acceleration of gravity as a function of height.
        """
        AccelOfGravity = c_AccelerationOfGravity * ((c_ConventionalRadius / (c_ConventionalRadius + Height)) ** 2)
        return AccelOfGravity


    def get_Temperature(self, Height):
        """
        Function for calculating temperature as a fucntion of height.
        """
        return 

    def get_Density(self, Height):
        """
        Function for calculating Density as a function of height.
        """
        return 
    
    def get_Pressure(self, Height):
        """
        Function for calculating pressure as a function of height.
        """
        return 

    def get_SoundSpeed(self, Height):
        """
        Function for calculating sound speed as a function of height.
        """
        return
