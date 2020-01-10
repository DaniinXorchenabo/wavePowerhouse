import numpy as np
from math import pi, sin, cos
from parameters import *
from functions import *






# h_vk_overWother = list(map(lambda i: i/10, h_vk_overWother))
print(h_vk)
print(float(sum(list([h_vk[i] * w_vk[i] * 0.005 for i in range(len(h_vk))])) / 22.4) * 8.31 * 60 * 1.5)

# print(w_vk)

x = np.arange(1,1000)/200 #+ pi/2 #629/200
h = np.around(A*np.sin(w*x -pi/2), decimals=3)



t = np.arange(2000)/200 # 0.005 секунды
dictt = {'x':x,'t':t}
def movement_wave(moment,last,u=listU[0]):
    x = dictt['x'] - (moment-last)*u
    S_go_mom = S_func(int(moment/0.005)-1)
#------
def moddifed_with_time(moment, last):
    movement_wave(moment,last)
last_time = 0
for i in t:
    try:
        moddifed_with_time(i,last_time)
        last_time = i
    except IndexError as e:
        print(e)
#------
    
#S = np.around(list(map(S_func, range(len(h)-1))), decimals=4)
#print(h)
#print(sum(S))
#S = -cos(x2) - (-cos(x1)) #площадь










