import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np

# points = []
#単位球の半径＝1cmと仮定

def select(num):
    points = []
    for i in range(num):  #range関数 range(stop値) 引数に指定した開始値から終了値までの連続した数値を要素として持つ
    #dt = np.pi/10
        t = random.random()  #random.random()（0.0以上1.0未満の浮動小数点数）tan(0°)~tan(90°)
        t = - np.arcsin(1-2*t)  #Θ
        u = random.random() * 2 * np.pi - np.pi #φ
    
        x = np.cos(t) * np.cos(u)
        y = np.cos(t) * np.sin(u)
        z = np.sin(t)
    
        points.append([x, y, z])  #points[i]に[x,y,z]の値を追加してく
    return  np.array(points)


# points = select(100)
# print(points)


# points = []
# for i in range(1000):  #range関数 range(stop値) 引数に指定した開始値から終了値までの連続した数値を要素として持つ
#     #dt = np.pi/10
#     t = random.random()  #random.random()（0.0以上1.0未満の浮動小数点数）tan(0°)~tan(90°)
#     t = - np.arcsin(1-2*t)  #Θ
#     u = random.random() * 2 * np.pi - np.pi #φ
    
#     x = np.cos(t) * np.cos(u)
#     y = np.cos(t) * np.sin(u)
#     z = np.sin(t)
    
#     points.append([x, y, z])  #points[i]に[x,y,z]の値を追加してく
# points = np.array(points)  #[[x0,y0,z0],[x1,y1,z1]]→[[x0,y0,z0] [x1,y1,z1]]のように、リストを行列にしてくれる。この場合、range数×3の行列ができる。

# fig = plt.figure(figsize=(15,15))  #2次元図を作成
# ax = Axes3D(fig)  #3次元にする
# ax.plot(points[:, 0], points[:,1], points[:, 2], "o", ms=2, mew=0.5) #[:,0]全ての行の0列目 ms=マーカーサイズ、mew=マーカーの枠線の太さ
# plt.show()