import numpy as np
from atmosphere import *
delta_elev_data = np.array([-26, -20, -10, -5, 0, 7.5, 15, 22.5, 28])*np.pi/180.0
CL_delta_elev_data = np.array([-0.132, -0.123, -0.082, -0.041, 0, 0.061, 0.116, 0.124, 0.137])
H = 500
atm = Atmosphere()
atm.set_H(H)
V = 200.0
Sw = 16.2 
m = 10**3
def get_ny(elevator_angle):
    q = atm.get_density()*V**2/(2.0*m)
    Cy=np.interp(elevator_angle,delta_elev_data,CL_delta_elev_data)
    return Cy*q*Sw    

