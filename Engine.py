import numpy as np
import math
"Раздел переменных, не инициализируемых в классе Двигатель"
"Скорость самолёта"
V_aircraft = 50
"Плотность воздуха на высоте 1500 м"
Air_density = 	1.0581
"Режим 1/0"
mode = 1
"Коэф-т J"
J = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94]
"Коэф-т Ct(J)"
Ct = [0.102122, 0.11097, 0.107621, 0.105191, 0.102446, 0.09947, 0.096775, 0.094706, 0.092341, 0.088912, 0.083878, 0.076336, 0.066669, 0.056342, 0.045688, 0.034716, 0.032492, 0.030253, 0.028001, 0.025735, 0.023453, 0.021159, 0.018852, 0.016529, 0.014194, 0.011843, 0.009479, 0.0071, 0.004686, 0.002278, -0.0002, -0.002638, -0.005145, -0.007641, -0.010188]
"функция вычисления текущего значения J"
def Get_Ct(J_new):
    return np.interp(J_new,J,Ct,Ct[0],Ct[-1])
"функция определения режима полёта"
def Get_mode(mode):
    if (mode == 0 or mode == 1):
        if (mode == 1):
            return 2*math.pi*2800/60
        else:
            return 2*math.pi*1000/60
    else:
        return "Mode must be 0 or 1"

"Класс двигатель"
class Engine(object):
    def __init__(self,propeller_R):
        self.propeller_R = propeller_R
    def get_tractive_power(self):
        omega = Get_mode(mode)
        print(omega)
        J_new = math.pi * V_aircraft / (omega * self.propeller_R)
        print(J_new)
        Ct_new = Get_Ct(J_new)
        return (4/(math.pi*math.pi))*Air_density*omega*omega*self.propeller_R*self.propeller_R*Ct_new

if __name__ == "__main__":
    eng = Engine(0.75)
    a = eng.get_tractive_power()
    print(a)