from parameters import *


def V_func():
    bmax = 100
    bmin = 10
    w_vk = [round((((len(h_vk) - i) / len(h_vk)) * (bmax - bmin) + 10) / 1000, 4) for i in range(len(h_vk))]

    count = 0
    ii = 0
    VVV = [h_vk[i] * w_vk[i] * 0.005 for i in range(len(h_vk))]
    for i in VVV:
        if sum(VVV) / 2 < count:
            break
        count += i
        ii = i
    print(ii, VVV.index(ii))


integrVolue = lambda mas, ind, wei: (mas[ind + 1] - mas[ind]) / 5 * (wei - ind * 5) + mas[ind]
F = lambda x, a=listA[0], w=listW[0],zerLev=zerLev[0] : -a*cos(w*x-pi/2)/w
S_func = lambda i,zerLev=zerLev[0]: F(x[i+1])-F(x[i]) - zerLev*(x[i+1]-x[i])

def getVHW(deepWave_mm, what='S'): # не работает как надоы
    try:
        ind1 = int(deepWave_mm/5)
        print(ind1)
        print(h_vk[ind1])
        if what == 'h':
            return integrVolue(h_vk,ind1,deepWave_mm)
        elif what == 'w':
            return integrVolue(w_vk,ind1,deepWave_mm)
        elif what == 'wh' or what == 'hw':
            return integrVolue(h_vk,ind1,deepWave_mm), integrVolue(w_vk,ind1,deepWave_mm)
        else:
            return integrVolue(h_vk,ind1,deepWave_mm)*integrVolue(w_vk,ind1,deepWave_mm)
        #setup_deep_h = integrVolue(h_vk,ind1,deepWave_mm)
        #setup_deep_w = integrVolue(w_vk,ind1,deepWave_mm)
    except Exception as e:
        print('-=-=-=-=-=-',e)
        return 'error in getVHW ' + str(e)

def fff(): # не работает
    a2 = []
    b2 = []
    z2 = []
    loc = a + a1
    locb = [(i//10) for i in b]
    ma = max(locb)
    mi = min(locb)
    print(locb)
    lenn = len(a + a1)
    [[(a2.extend([a[i]]*int(j) + [a1[i]]*int(j)),
       b2.extend([(ma+mi)/2*j/2*j1 for j1 in range(-int(j),int(j),2)]*2), z2.extend([i]*int(j) + [i]*int(j))
       ) for j in locb]
     for i in range(5,6)]
    print(len(a2), len(b2), len(z2))
    return a2,b2,z2
#a2,b2,z2 = fff()