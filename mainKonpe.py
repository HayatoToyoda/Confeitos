#各関数ファイルをインポートし、結果をアウトプットするためのファイル
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import function.distance as distance
import function.SelectPoint as SelectPoint
import function.shift2 as shift
import csv
import math

#このプログラムでは、「時間」パラメータは処理回数として取り扱っている。「時間」はシミュレーションで得られた半径の値を元に、実験で得られた半径と時間の関係式を用いて求めている

points = []  #空リスト作成（初期化）
num = 98 #実験開始から２時間 本当は97.8本
dr = 0.2204  #cm。実験開始から２時間
m = 0 #半径の増加定数
r = 0.4916 #cm 実験開始から２時間
f = open('num=98_d_r_change.csv' , 'w')
header = [['points(本)','dr(cm)','r(cm)']]
body = [[num,dr,r]]
writer = csv.writer(f, lineterminator='\n')
writer.writerows(header)
writer.writerows(body)




#----------------処理-------------------

#初回の角生成
points = SelectPoint.select(num,r)  

fig = plt.figure(figsize=(15,15))  
ax = Axes3D(fig)  

#初回の角の状態を3Dにプロット
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,color="white",rcount=100, ccount=100, antialiased=False,alpha = 0.1)
ax.plot(points[:, 0], points[:,1], points[:, 2],"*", ms=5, mew=0.5)

for i in range(num):
  
  #角ごとに、周囲に存在する全ての角との間隔を測定。
  dMatrix = distance.measure(num,points)

  dnum = 0
  dcount = 0

  #結合を継続するかどうかの判定
  # for i in range(len(dMatrix)):
  #   for j in range(len(dMatrix)):
  #     if(dMatrix[i][j] < dr):
  #       dnum = dnum + 1
  # if(dnum == 0):
  #   break

  if(num < 24):
    break

  
  #どの角を結合させるかどうか？の情報をindexに格納
  index = shift.index(num,dMatrix)
  
  #mix関数内のcenter関数で結合処理を行い、mixでは結合した点とそうでない点の数を合計する▶結合処理後の角の総数
  points = shift.mix(index,points,m)

  #m:半径の時間変化。center関数とmix関数に渡す
  m = m + 0.0412
  r = r + m
  dr = 0.3658 * math.log(r) + 0.4835 #１回転でのdrの変化
  



  num = len(points)
  

  body = [[num,'{:.04f}'.format(dr),'{:.04f}'.format(r)]]
  writer.writerows(body)

f.close()


# fig = plt.figure(figsize=(15,15))  
# ax = Axes3D(fig)  

#最終的な角の状態をプロット
ax.plot(points[:, 0], points[:,1], points[:, 2],"o", ms=5, mew=0.5)
plt.show()



