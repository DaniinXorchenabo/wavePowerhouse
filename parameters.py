from math import pi, sin, cos

h_vk = [1157, 1137, 1126, 1114, 1104, 1089, 1075, 1056, 1047, 1030, 1013, 997, 979, 968, 946, 927, 909, 894, 879, 865,
        850, 830, 821, 805, 789, 776, 766, 746, 733, 722, 703, 686, 670, 657, 635, 621, 596, 573, 548, 516, 488, 445,
        398, 337, 264, 152, 0]  # a мм

h_vk_overWother = [1157, 1135, 1127, 1110, 1100, 1087, 1075, 1060, 1051, 1041, 1029, 1020, 1009, 999, 995, 994, 984,
                   978, 975, 974, 973, 973, 978, 980, 985, 994, 1005, 1016, 1023, 1036, 1050, 1066, 1084, 1104, 1125,
                   1157, 1172, 1193, 1221, 1253, 1285, 1317, 1347, 1391, 1436, 1475, 1475]  # a1
h_vk = [i / 10000 for i in h_vk]
h_vk_overWother = [i / 10000 for i in h_vk_overWother]
h_underVk = [h_vk_overWother[i] - h_vk[i] for i in range(len(h_vk))]
bmax, bmin = 100, 10
w_vk = [round((((len(h_vk) - i) / len(h_vk)) * (bmax - bmin) + 10) / 1000, 4) for i in range(len(h_vk))]



waveZeroLevel = -0.5
zerLev = [waveZeroLevel]
A = 0.5
listA = [A]
T = 20  # = L/u (длинна на скорость распростронения)
L = 10  # длинна волны
u = L/T
listU = [u]
w = 2*pi/T
listW = [w]
