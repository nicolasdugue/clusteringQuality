#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from scipy.sparse import coo_matrix
import itertools

class Comparateur:
	def __init__(self, clustering1, clustering2):

		self.c1 = clustering1
		self.c2 = clustering2
		row=[]
		col=[]
		data=[]
		row2=[]
		col2=[]
		data2=[]
		taille=len(self.c1)
		for id1 in range(taille):
		    for id2 in range(id1 +1, taille):
		        if self.c1[id1] == self.c1[id2]:
		            row.append(id1)
		            col.append(id2)
		            data.append(1)
		        if self.c2[id1] == self.c2[id2]:
		            row2.append(id1)
		            col2.append(id2)
		            data2.append(1)
		self.c1_m=coo_matrix((data, (row, col)), shape=(taille, taille))
		self.c2_m=coo_matrix((data2, (row2, col2)), shape=(taille, taille))


	def get_dot_product(self):
		dot=0
		c2=self.c2_m.tocsr()
		for i,j,v in itertools.izip(self.c1_m.row, self.c1_m.col, self.c1_m.data):
			if c2[i,j] != 0:
				dot+=1
		return dot

	def get_dot_c1(self):
		return len(self.c1_m.data)

	def get_dot_c2(self):
		return len(self.c2_m.data)

	def get_correlation(self):
		print (self.get_dot_product(), self.get_dot_c1(), self.get_dot_c2())
		return self.get_dot_product() / sqrt(self.get_dot_c1() * self.get_dot_c2())

test=Comparateur([0,0,1,1], [0,1,0,1])
print(test.get_correlation())
test=Comparateur([0,0,1,1], [0,0,0,0])
print(test.get_correlation())
test=Comparateur([1,1,1,1], [0,1,0,1])
print(test.get_correlation())
test=Comparateur([1,0,1,0], [0,1,0,1])
print(test.get_correlation())
test=Comparateur([0,1,0,1], [0,1,0,1])
print(test.get_correlation())
test=Comparateur([0,0,0,1], [1,0,0,1])
print(test.get_correlation())
test=Comparateur([0,0,1,1], [1,1,0,0])
print(test.get_correlation())
test=Comparateur([0,0,1,2], [1,1,0,2])
print(test.get_correlation())
