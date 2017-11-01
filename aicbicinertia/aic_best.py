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
    center=FileReader.read_cod(cod)
    inertia=0
    for idx, vect in enumerate(data):
        dist=minkowski(vect,center[clustering[idx]],1)
        inertia+=dist *  dist
    K,M=(len(center[0]), len(center))
    return inertia + 2*M*K


data_dir="data"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]

for exp in data_dirs:
    X = [join(exp,f) for f in listdir(exp) if ".nrm" in f]
    X=FileReader.read_dat(X[0]).toarray()
    cods = [join(exp,f) for f in listdir(exp) if ".cod" in f]
    cods.sort()
    elms = [join(exp,f) for f in listdir(exp) if ".elm" in f]
    elms.sort()
    lowest_aic = np.infty
    dico_aic = dict()
    n_best=0
    R, M = X.shape
    for elm,cod in zip(elms,cods):
        clustering=FileReader.read_elm(elm)
        n_components=len(set(clustering))
        aic=aic_k_best(X, clustering, cod)
        if n_components not in dico_aic or aic < dico_aic[n_components]:
            dico_aic[n_components]=aic
        if aic < lowest_aic:
            lowest_aic = aic
            n_best=n_components
    print (exp,lowest_aic, n_best)
