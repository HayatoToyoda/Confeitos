import numpy as np
import random
import math
import copy
from numpy.lib.function_base import append
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
import csv
 


def index(num,dMatposs):

  ind = []
  for i in range(num):
    j = np.where(dMatposs[i] == min(dMatposs[i]))
    if(dMatposs[i][j[0][0]] == min(dMatposs[j[0][0]])):
      ind.append([i,j[0][0]])
  return ind




def center(points,ind):

  centerP = []
  
  for i in range(len(ind)) :
    x = (points[(ind[i][0])][0] + points[(ind[i][1])][0]) / 2.0
    y = (points[(ind[i][0])][1] + points[(ind[i][1])][1]) / 2.0
    z = (points[(ind[i][0])][2] + points[(ind[i][1])][2]) / 2.0

    centerP.append([x,y,z])
  
  centerP = np.array(centerP)
  centerP = np.unique(centerP,axis=0)
  return centerP

def mix(ind,points):
  newPoints = []
  centerP = center(points,ind)
  ind = list(itertools.chain.from_iterable(ind))
  ind = np.unique(ind)  

  for i in range(len(ind)):
    points[ind[i]] = 7474
  
  c = np.concatenate((points,centerP), axis = 0) 
  newPoints = np.delete(c,np.where(c == 7474)[0],axis=0)
  return newPoints