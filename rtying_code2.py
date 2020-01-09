import plotly
import plotly.graph_objs as go
import numpy as np
h_vk = [1157,1137,1126, 1114,1104, 1089,1075,1056,1047, 1030, 1013, 997,979, 968,946, 927,909, 894,879,865,850,830,821,805,789, 776, 766,746,733,722,703, 686,  670,657,635,621,596, 573,548, 516, 488,445,398,337,264, 152,0]#a
h_vk_overWother = [1157,1135,1127,1110,1100,1087,1075,1060,1051,1041,1029,1020,1009, 999, 995,994,984,978,975,974,973,973,978,980,985,994,1005,1016,1023,1036,1050,1066,1084,1104,1125,1157,1172,1193,1221,1253,1285,1317,1347,1391,1436,1475,1475] #a1
h_underVk = [h_vk_overWother[i] - h_vk[i] for i in range(len(h_vk))]
bmax = 100
bmin = 10
h_vk_overWother = list(map(lambda i: i/10, h_vk_overWother))
w_vk = [round((((len(h_vk) - i)/len(h_vk))*(bmax-bmin) + 10)*10, 1) for i in range(len(h_vk))]
integrVolue = lambda mas, ind, wei: (mas[ind+1] - mas[ind])/5*(wei - ind*5)+ mas[ind]


#----=-=-=-


print('hellow_comit')
print('test2')



def getVHW(deepWave_mm, what='V'):
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

print(h_vk)
print(getVHW(12.456))

a1 = [i + 10 for i in h_vk_overWother]
a1 = [1500-i for i in a1]
a = [1500-i for i in h_vk]

b = [round(((len(a) - i)/len(a))*(bmax-bmin) + 10, 1) for i in range(len(a))]
print(len(b), len(a), len(a1))

def fff():
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

x = np.arange(500)/500 + np.arange(500)/500 + np.arange(500)/500 + np.arange(500)/500 + np.arange(500)/500
y = (np.arange(len(a) + len(a1))*0)# + (np.arange(500)*0) + 1 + (np.arange(500)*0) + 2 + (np.arange(500)*0) + 3 + 
d = np.random.randint(low=1, high=100, size=500)/10
e = np.random.randint(low=10, high=100, size=500)/10


fig1 = go.Scatter3d(x=z2,
                    y=a2,
                    z=b2,
                    marker=dict(opacity=0.9,
                                reversescale=True,
                                colorscale='Blues',
                                size=5),
                    line=dict (width=0.02),
                    mode='lines+markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="x"),
                                yaxis=dict( title="y"),
                                zaxis=dict(title="z")),)

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("3DPlot.html"))