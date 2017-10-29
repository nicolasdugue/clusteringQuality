#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import cluster
import numpy as np
import itertools

from scipy import linalg
import sklearn.datasets
from sklearn.cluster import KMeans

from scipy.spatial.distance import minkowski
import sys
sys.path.append("common/ioreader")
import FileReader

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

data_dir="data"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]

for exp in data_dirs:
    if "R52" in exp or "R8" in exp:
        continue
    X = [join(exp,f) for f in listdir(exp) if ".nrm" in f]
    X=FileReader.read_dat(X[0]).toarray()
    cod = [join(exp,f) for f in listdir(exp) if ".cod" in f][0]
    elm = FileReader.read_elm([join(exp,f) for f in listdir(exp) if ".elm" in f][0])
    print(exp, len(set(elm)),aic_k_best(X, elm, cod))
    lowest_aic = np.infty
    dico_aic = dict()
    n_best=0
    R, M = X.shape
    if "IRIS" in exp:
        n_components_range = range(2, 10)
    elif "PEN" in exp:
        n_components_range = range(2, 30)
    elif "WINE" in exp:
        n_components_range = range(2, 10)
    elif "SOY" in exp:
        n_components_range = range(2, 50)
    elif "ZOO" in exp:
        n_components_range = range(2, 22)
    elif "VRBF" in exp:
        n_components_range = range(2, 50)
    else:
        n_components_range = range(2, 10)
    for n_components in n_components_range:
        kmeansi = KMeans(n_clusters=n_components, init='random',n_init=50).fit(X)
        aic=aic_k(kmeansi, n_components, M)
        if n_components not in dico_aic or aic < dico_aic[n_components]:
            dico_aic[n_components]=aic
        if aic < lowest_aic:
            lowest_aic = aic
            n_best=n_components
    print (exp,lowest_aic, n_best)
