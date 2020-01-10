import numpy as np
from math import pi, sin, cos
from parameters import *
from functions import *



print(h_vk)


x = np.arange(1,1000)/200 #+ pi/2 #629/200
h = np.around(A*np.sin(w*x -pi/2), decimals=3)
t = np.arange(2000)/200 # 0.005 секунды
# S = np.around(list(map(S_func, range(len(h)-1))), decimals=4)


dictt = {'x':x,'t':t}
def movement_wave(moment,last,u=listU[0]):
    x = dictt['x'] - (moment-last)*u
    S_go_mom = S_func(int(moment/0.005)-1)

def moddifed_with_time(moment, last):
    movement_wave(moment,last)
last_time = 0
for i in t:
    try:
        moddifed_with_time(i,last_time)
        last_time = i
    except IndexError as e:
        print(e)










