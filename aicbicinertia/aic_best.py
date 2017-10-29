#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import cluster
import numpy as np
import itertools

from scipy import linalg
import sklearn.datasets
from sklearn.cluster import KMeans

from scipy.spatial.distance import minkowski
import code.io.FileReader as fr

def aic_k_best(data, clustering, cod):
    center=np.loadtxt(open(cod, "r"), delimiter=" ", skiprows=1)
    inertia=0
    for idx, vect in enumerate(data):
        dist=minkowski(vect,center[clustering[idx]],1)
        inertia+=dist *  dist
    K,M=center.shape
    return inertia + 2*M*K

def aic_k(kmeansi, K, M):
    return kmeansi.inertia_ + 2*M*K

# IRIS DATA
#iris = sklearn.datasets.load_iris()
#X = iris.data[:, :4]  # extract only the features
#Y = iris.target
#size of data set
#R, M = X.shape

data_dir="/home/dugue/Bureau/aa-PackNicoAPIN"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]

for exp in data_dirs:
    X = [join(exp,f) for f in listdir(exp) if ".nrm" in f]
    X=fr.read_dat(X[0]).toarray()
    cods = [join(exp,f) for f in listdir(exp) if ".cod" in f]
    lowest_aic = np.infty
    dico_aic = dict()
    n_best=0
    R, M = X.shape
    for cod in cods:
        aic=aic_k(kmeansi, n_components, M)
        if n_components not in dico_aic or aic < dico_aic[n_components]:
            dico_aic[n_components]=aic
        if aic < lowest_aic:
            lowest_aic = aic
            n_best=n_components
    print (exp,lowest_aic, n_best)
