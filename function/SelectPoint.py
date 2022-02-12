import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np

#単位球の半径＝0.43205cm



def select(num,r):
    points = []
    for i in range(num):  #range関数 range(stop値) 引数に指定した開始値から終了値までの連続した数値を要素として持つ
    #dt = np.pi/10
        t = random.random()  #random.random()（0.0以上1.0未満の浮動小数点数）tan(0°)~tan(90°)
        t = - np.arcsin(1-2*t)  #Θ
        u = random.random() * 2 * np.pi - np.pi #φ
    
        x = np.cos(t) * np.cos(u) * r
        y = np.cos(t) * np.sin(u) * r
        z = np.sin(t) * r


    
        points.append([x, y, z])  #points[i]に[x,y,z]の値を追加してく
    return  np.array(points)



