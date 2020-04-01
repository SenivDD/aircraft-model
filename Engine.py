import numpy as np
from math import pi
from atmosphere import *
atm = Atmosphere()
atm.set_H(1500)
"Раздел переменных, не инициализируемых в классе Двигатель"
"Скорость самолёта"
V_aircraft = 50
Air_density = 	atm.get_density()
"Режим 1/0"
mode = 1
mode_arr = [0 1]
omega_arr [1000 2800]
"Коэф-т J"
J = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94]
"Коэф-т Ct(J)"
Ct = [0.102122, 0.11097, 0.107621, 0.105191, 0.102446, 0.09947, 0.096775, 0.094706, 0.092341, 0.088912, 0.083878, 0.076336, 0.066669, 0.056342, 0.045688, 0.034716, 0.032492, 0.030253, 0.028001, 0.025735, 0.023453, 0.021159, 0.018852, 0.016529, 0.014194, 0.011843, 0.009479, 0.0071, 0.004686, 0.002278, -0.0002, -0.002638, -0.005145, -0.007641, -0.010188]

"функция определения режима полёта"


"Класс двигатель"
class Engine(object):
    def __init__(self,propeller_R = 0.94):
        self.propeller_R = propeller_R

    def Get_mode(self,mode):
            return  2*pi*(np.interp(mode,mode_arr,omega_arr,omega_arr[0],omega_arr[-1]))/60

    def get_tractive_power(self):
        omega = self.Get_mode(mode)
        J_new = pi * V_aircraft / (omega * self.propeller_R)
        Ct_new = self.Get_Ct(J_new)
        return (2/pi)**2*Air_density*(omega*self.propeller_R)**2*Ct_new
    "функция вычисления текущего значения Ct"
    def Get_Ct(self,J_new):
        return np.interp(J_new,J,Ct,Ct[0],Ct[-1])


eng = Engine()
a = eng.get_tractive_power()
print(a)