from atm_consts import *

class Atmosphere:
    """
    This class will contain model of the atmosphere according to GOST - 4401-81
    """
    def get_accel_of_gravity(self, height):
        """
        Function for calculating the acceleration of gravity as a function of height.
        """
        accel_of_gravity = ACCELERATION_OF_GRAVITY * ((CONVENTIONAL_RADIUS / (CONVENTIONAL_RADIUS + height)) ** 2)
        return accel_of_gravity

    def set_geopotentional_height(self, height):
        """
        Function for converting geometric height to geopotential height.
        """
        geopotential_height = (CONVENTIONAL_RADIUS * height) / (CONVENTIONAL_RADIUS + height)
        
        return geopotential_height

    
    def get_temperature(self, height):
        """
        Function for calculating temperature as a fucntion of height.
        """
        return 

    def get_density(self, height):
        """
        Function for calculating Density as a function of height.
        """
        return 
    
    def get_pressure(self, height):
        """
        Function for calculating pressure as a function of height.
        """
        return 

    def get_sound_speed(self, height):
        """
        Function for calculating sound speed as a function of height.
        """
        return
