import numpy as np
import math


#----------------距離を求める関数(clear)-----------------
def measure(num,points):
  dMatrix = np.identity(num)  #求めたdを入れるための単位行列作成
  for i in range(num):  #行方向の数
    for j in range(num):  #列方向の数
      d = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2 + (points[i][2]-points[j][2])**2
      d = np.abs(math.sqrt(d))  
     #print(d)  手動で計算機使ったものと比較しても一致。
      if(d == 0):  
        x = 1000  #以下で最小値を求める際、0だと不都合だから
        dMatrix[i][j] = x
      else:
       dMatrix[i][j] = d
      #  if((i!=j) & (dMatrix[i][j] == dMatrix[j][i])):  #重複を考えないため
      #   dMatrix[i][j] = 200  
  
  return dMatrix
#---------------------------------