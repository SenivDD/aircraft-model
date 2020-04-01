import numpy as np
from model_function_upr import *
from matplotlib import pyplot as plt


#ny_tek = 0 # начальное значение перегрузки
#ny_zad = 3
#k = 0.01

#def get_angle_wheel (self) :
    
ny_tek = 0 # начальное значение перегрузки
eliv_new = 0 # начальное положение угла руля высоты
ny_zad = 10
k = 0.001
t = 0
i = 0
y_eliv_new = []
y_ny_tek = []
y_ny_zad = []
x_t = []

output = open("output.txt", "w")

output.write("t         eliv_new  ny_tek \n")

while ((abs(ny_tek - ny_zad) > 0.01) and (t <= 10)) :
#while (ny_tek != ny_zad) :
    
    x_t.append(t)
    y_eliv_new.append(eliv_new*180.0/np.pi)
    y_ny_tek.append(ny_tek)
    y_ny_zad.append(ny_zad)

    #print ('eliv_new = ', eliv_new)
    #print ('ny_tek = ', ny_tek)
    #print ('t = ', t)
    #print ('')

    output.write ( "{:f}  {:f}  {:f}\n".format(t, eliv_new*180.0/np.pi, ny_tek) )

    #eliv_new = eliv_last + k*(ny_zad-ny_tek)
    ny_tek = get_ny(eliv_new)/ACCELERATION_OF_GRAVITY
    eliv_new = eliv_new + k*(ny_zad-ny_tek)

    if (eliv_new* 180.0/np.pi >= 26) :
        eliv_new = 26/180.0*np.pi

    if (eliv_new* 180.0/np.pi <= -28) :
        eliv_new = -28/180.0*np.pi
    #eliv_new = eliv_new * 180.0/np.pi
    
    #eliv_last = eliv_new
    t = t + 0.02

    

    #print ('eliv_last = ', eliv_last)


#fig = plt.figure()
output.close()

fig1 = plt.figure()
plt.title("Изменение отклонения руля высоты")
plt.xlabel ("Время наблюдения, [c]")
plt.ylabel ("Угол текущего положения рулей, [град]")
plt.plot (x_t, y_eliv_new)
plt.grid()

fig2 = plt.figure()
plt.title("Изменение значения перегрузки")
plt.xlabel ("Время наблюдения, [c]")
plt.ylabel ("Перегрузка, []")
plt.plot (x_t, y_ny_tek)
plt.plot (x_t, y_ny_zad)
plt.grid()

plt.show()
           
 #   return eliv_new
