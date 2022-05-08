import sys
import math
from abc import ABC,abstractmethod
from geometry import * 
from material import *
from math  import sin,atan2,asin,pi
import numpy as np 

# abstract texture base class
class texture(ABC):
	def __init__(self):
		pass
	def value(u: float, v: float, p: vec3):
		pass 

class constant_texture(texture): 
	def __init__(self, color: vec3):
		self.color = color
	def value(self, u: float, v: float, p: vec3):
		return self.color

class checker_texture(texture):
	def __init__(self, texture1: texture, texture2: texture):
		self.even,self.odd = texture1,texture2
	def value(self,u: float, v: float, p: vec3):
		sines = float(sin(10 * p[0]) * sin(10 * p[1]) * sin(10 * p[2]))
		if sines < 0: 
			return self.odd.value(u,v,p)
		else:
			return self.even.value(u,v,p)

class image_texture(texture):
	def __init__(self,image: np.array,A: int, B: int):
		#convert to list because pixel lookup in numpy array is very slow 
		self.data = image[:,:,:3].tolist()
		self.nx = A 
		self.ny = B
	def value(self,u: float, v: float, p: vec3):
		i = u * self.nx
		j = (1 - v) * self.ny - 0.001
		i = int(max(0,min(i,self.nx - 1)))
		j = int(max(0,min(j, self.ny - 1)))

		r,g,b = self.data[i][j]
		# print(vec3(r,g,b))
		return vec3(r,g,b)


