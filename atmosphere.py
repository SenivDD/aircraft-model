from atm_consts import *
from math import log10
class Atmosphere:
    """
    This class will contain model of the atmosphere according to GOST - 4401-81
    """
    def __init__(self,T_base=288.15,H_base=0.0,pressure_base=101325.0):
        self.T_base = T_base
        self.H_base = H_base
        self.pressure_base = pressure_base
  
    def set_H(self,H_in):
        self.H = H_in
        self.H_geo = (CONVENTIONAL_RADIUS * self.H) / (CONVENTIONAL_RADIUS + self.H)
        self.accel_of_gravity = ACCELERATION_OF_GRAVITY * ((CONVENTIONAL_RADIUS / (CONVENTIONAL_RADIUS + self.H)) ** 2)
        self.T = self.T_base +T_GRAD*(self.H_geo-self.H_base)
        self.pressure = self.pressure_base*10**(-ACCELERATION_OF_GRAVITY/(T_GRAD * SPECIFIC_GAS_CONST)*log10(self.T/self.T_base))
        self.Density = self.pressure * MOLAR_MASS/(self.T * UNIVRSAL_GAS_CONST) 
        sef.V_sound = 20.046796*self.T**0.5

    def get_accel_of_gravity(self, height):
        """
        Function for calculating the acceleration of gravity as a function of height.
        """
        return accel_of_gravity 

    def get_temperature(self):
        """
        Function for calculating temperature as a fucntion of height.
        """
        return self.T

    def get_density(self):
        """
        Function for calculating Density as a function of height.
        """
        return self.Density
    
    def get_pressure(self):
        """
        Function for calculating pressure as a function of height.
        """
        return self.pressure

    def get_sound_speed(self):
        """
        Function for calculating sound speed as a function of height.
        """
        return self.V_sound
