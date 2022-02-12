import numpy as np
import random
import math
import copy
from numpy.lib.function_base import append
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
import csv
 


#結合しそうな角の間隔データを保有する点のインデックス番号を保存するための関数。どの角を結合させるべきか？の判定に用いる
def index(num,dMatposs):

  ind = []
  for i in range(num):
    j = np.where(dMatposs[i] == min(dMatposs[i]))
    if(dMatposs[i][j[0][0]] == min(dMatposs[j[0][0]])):
      ind.append([i,j[0][0]])
  return ind




#2点間の直線距離を求め、２点の弧の上に中点を配置
def center(points,ind,m):

  centerP = []
  
  for i in range(len(ind)) :
    xc = (points[(ind[i][0])][0] + points[(ind[i][1])][0]) / 2.0
    yc = (points[(ind[i][0])][1] + points[(ind[i][1])][1]) / 2.0
    zc = (points[(ind[i][0])][2] + points[(ind[i][1])][2]) / 2.0

    #座標を球面上の点とするために正規化。引数mは時間変化に応じて
    Normalize = np.sqrt(xc*xc + yc*yc + zc*zc) + m
    x = (xc / Normalize) 
    y = (yc / Normalize) 
    z = (zc / Normalize) 

    centerP.append([x,y,z])
  
  centerP = np.array(centerP)
  centerP = np.unique(centerP,axis=0)
  return centerP

#新しくできた角と結合が見られなかった角の本数を合計する
def mix(ind,points,m):
  newPoints = []
  centerP = center(points,ind,m)
  ind = list(itertools.chain.from_iterable(ind))
  ind = np.unique(ind)  

  for i in range(len(ind)):
    points[ind[i]] = 7474
  
  c = np.concatenate((points,centerP), axis = 0) 
  newPoints = np.delete(c,np.where(c == 7474)[0],axis=0)
  return newPoints