#各関数ファイルをインポートし、結果をアウトプットするためのファイル
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import function.distance as distance
import function.SelectPoint as SelectPoint
import function.shift2 as shift
import csv

points = []  #空リスト作成（初期化）
num = 1000
dr = 0.4  #単位はcmで統一。
count = 0
f = open('d=0.4.csv' , 'w')
header = [['count','points','dr']]
body = [[count,num,dr]]
writer = csv.writer(f, lineterminator='\n')
writer.writerows(header)
writer.writerows(body)



#----------------処理-------------------

points = SelectPoint.select(num)  

for i in range(num):
  

  dMatrix = distance.measure(num,points)

  dnum = 0
  for i in range(len(dMatrix)):
    for j in range(len(dMatrix)):
      if(dMatrix[i][j] < dr):
        dnum = dnum + 1
  if(dnum == 0):
    break
 
  index = shift.index(num,dMatrix)
  points = shift.mix(index,points)


  num = len(points)
  count = count + 1
  

  body = [[count,num,dr]]
  writer.writerows(body)

f.close()


fig = plt.figure(figsize=(15,15))  
ax = Axes3D(fig)  
ax.plot(points[:, 0], points[:,1], points[:, 2], "o", ms=2, mew=0.5)
plt.show()



