#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.sparse import csr_matrix, csc_matrix
import numpy as np
from math import log, pi, e

import logging


class quality:
	def __init__(self, data, clustering, labels_row=[], labels_col=[]):
		"""
		Matrix (data) and clustering should be at least passed.
		Matrix should be a 2D Array or already a sparse (csr or csc) matrix.
		Clustering should be an array where a value v at index i defines that the object i (row i in matrix) belongs to cluster v
		Labels can be used to describe rows (objects) and columns (features) in the same way as the clustering object
		"""
		self.logger = logging.getLogger("Main")

		self.data = csr_matrix(data)
		#self.logger.debug("data : "+str(self.data.toarray()))
		self.clustering = clustering

		self.clusters=[]
		for idx,elmt in enumerate(self.clustering):
			elmt=int(elmt)
			taille=(len(self.clusters) -1)
			if elmt >= taille:
				for i in range(elmt - taille):
					self.clusters.append([])
			self.clusters[elmt].append(idx)

		self.labels_row=labels_row

		self.labels_col=labels_col

		self.sum_rows=self.data.sum(axis=1)

		self.sum_cols=self.data.sum(axis=0)

		self.data=self.data.toarray()



	def sum_row(self, i):
		"""
		Get the sum of row i
			"""
		return self.sum_rows[i]

	def sum_col(self, j):
		"""
		Get the sum of column j
		Used in Feature Precision (Predominance)
			"""
		return self.sum_cols[:,j]

	def sum_cluster(self, i):
		"""
		Get the sum of cluster i
		Used in feature recall
		"""
		cluster=self.clusters[i]
		som=0
		for row in cluster:
			som+=self.sum_row(row)
		return som

	def get_row_label(self, i):
		"""
		Get the label of row i
		"""
		if len(self.labels_row) == len(self.clustering):
			return self.labels_row[i]
		else:
			return i+""

	def get_col_label(self, j):
		"""
		Get the label of col j
		"""
		if len(self.labels_col) > 0:
			return self.labels_col[j]
		else:
			return j+""

	def get_nb_data(self):
		return len(self.clustering)

	def get_size_cluster(self, k):
		return len(self.clusters[k])

	def get_nb_cluster(self):
		return len(self.clusters)

	def get_pi(self,i):
		return float(self.get_size_cluster(i)) / self.get_nb_data()

	def get_sigma0(self):
		cov=np.cov(np.matrix(self.data).T)
		sign, logdet =np.linalg.slogdet(cov)
		self.logger.debug("cov : " + str(cov.shape))
		self.logger.debug("Signe : " + str(sign))
		self.logger.debug("logdet sigma0 : "+str(logdet))
		return logdet

	def get_sigma_i(self, i):
		list_vi=self.clusters[i]
		si=[]
		self.logger.debug("iiiiiiiiiiiiii : "+str(i))
		for vi in list_vi:
			si.append(self.data[vi])
		#self.logger.debug("matrix i : \n"+self.get_str_matrice(np.matrix(si)))
		#Get the transpose to work on the features
		cov=np.cov(np.matrix(si).T)
		#self.logger.debug("cov sigmai :\n" +self.get_str_matrice(cov))
		sign, logdet = np.linalg.slogdet(cov)
		self.logger.debug("Signe : " + str(sign))
		self.logger.debug("logdet sigma "+str(i)+" : "+str(logdet))
		return logdet

	def get_negentropy(self):
		sum=0
		sum2=0
		for i_clust in range(self.get_nb_cluster()):
			pi=self.get_pi(i_clust)
			self.logger.debug("i : "+str(i_clust)+ str(", pi : ")+ str(pi)+ str(", ni : ")+ str(self.get_size_cluster(i_clust))+", n : "+str(self.get_nb_data()))
			sum+= pi * self.get_sigma_i(i_clust)
			sum2-= pi * log(pi)
		sum-=self.get_sigma0()
		sum*=0.5
		sum+=sum2
		return sum

	def get_negentropy_us(self):
		sum=0
		sum2=0
		for i_clust in range(self.get_nb_cluster()):
			pi=self.get_pi(i_clust)
			ni=self.get_size_cluster(i_clust)
			self.logger.debug("i : "+str(i_clust)+ str(", pi : ")+ str(pi)+ str(", ni : ")+ str(self.get_size_cluster(i_clust))+", n : "+str(self.get_nb_data()))
			sum+= 0.5*pi * self.get_sigma_i(i_clust)
			sum+= pi*pi*ni * log(pi)
			sum+=pi*ni*log(2*pi*e)
		sum-=0.5*self.get_sigma0()
		sum-=(self.get_nb_data()/(2.0))*log(2*pi*e)
		return sum

	def get_str_matrice(self,data):
		chaine=""
		for i in data:
			for j in i:
				chaine+=" "+str(j)
			chaine+="\n"
		return chaine
