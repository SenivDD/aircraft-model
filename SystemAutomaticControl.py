import numpy as np
from model_function_upr import *
from matplotlib import pyplot as plt

array_eliv = []     # массив значений отклонения руля (угол отклонения руля [град])
array_ny_now = []   # массив значений перегрузок в данный момент времени
array_ny_spec = []  # массив значений заданной перегрузки (постоянная)
array_t = []        # массив значений времени

eps_ny = 0.01       # |(ny_now - ny_spec)| > eps_ny

# Функция получения положения руля высоты и текущей перегрузки 
#   ny_spec - заданное значение перегрузки   
def get_eliv_and_ny_new (ny_spec) :
    
    global array_eliv
    global array_ny_now
    global array_ny_spec
    global array_t

    array_eliv.clear()
    array_ny_now.clear()
    array_ny_spec.clear()
    array_t.clear()
    
    ny_now = 0 # начальное значение перегрузки
    eliv_new = 0 # начальное положение угла руля высоты
    k = 0.001
    t = 0
    i = 0

    while ((abs(ny_now - ny_spec) > eps_ny) and (t <= 10)) :
    #while (ny_now != ny_spec) :
    
        array_t.append(t)
        array_eliv.append(eliv_new*180.0/np.pi)
        array_ny_now.append(ny_now)
        array_ny_spec.append(ny_spec)

        ny_now = get_ny(eliv_new) / ACCELERATION_OF_GRAVITY
        eliv_new = eliv_new + k * (ny_spec - ny_now)

        if (eliv_new * 180.0/np.pi >= 26) :
            eliv_new = 26/180.0*np.pi

        if (eliv_new * 180.0/np.pi <= -28) :
            eliv_new = -28/180.0*np.pi

        t = t + 0.02
        
    return eliv_new, array_eliv

# Функция записи в файл полученных результатов 
#   filename - имя файла для записи
#   ny_spec - заданное значение перегрузки 
def WriteToFile (filename, ny_spec) :
   
    get_eliv_and_ny_new (ny_spec)
   
    np.savetxt(filename, 
        np.column_stack((array_t, array_eliv, array_ny_now)), 
        fmt = '%5.2f | %8.5f | %8.5f', 
        header = ('Для перегрузки = ' + str(ny_spec) + '\nt   | eliv_new |  ny_now\n-------------------------'), 
        delimiter = ' | ')
    
    return
    
fig1 = plt.figure()
plt.title("Изменение отклонения руля высоты")
plt.xlabel ("Время наблюдения, [c]")
plt.ylabel ("Угол текущего положения рулей, [град]")

for i in range(1, 6, 2): # цикл от 1 до 5 с шагом 2, 
    #i - значения перегрузки
    get_eliv_and_ny_new (i)
    plt.plot (array_t, array_eliv, label = 'Заданная перегрузка = ' + str(i))
    print("\ni = ", i)

plt.legend()
plt.grid()

fig2 = plt.figure()
get_eliv_and_ny_new (1)
plt.title("Изменение значения перегрузки")
plt.xlabel ("Время наблюдения, [c]")
plt.ylabel ("Перегрузка, []")
plt.plot (array_t, array_ny_now, label = 'Текущая перегрузка')
plt.plot (array_t, array_ny_spec, label = 'Заданная перегрузка')
plt.legend()
plt.grid()
plt.show()

WriteToFile ("output1.txt", 1)
WriteToFile ("output3.txt", 3)
WriteToFile ("output5.txt", 5)
