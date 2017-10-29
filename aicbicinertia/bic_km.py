#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import cluster
import numpy as np
import itertools
from math import log

from scipy import linalg
import sklearn.datasets
from sklearn.cluster import KMeans

from scipy.spatial.distance import minkowski
import sys
sys.path.append("common/ioreader")
import FileReader

def bic_k(kmeansi,r, k ,m):
    center=kmeansi.cluster_centers_
    label=kmeansi.labels_
    inertia=kmeansi.inertia_
    return (r*log(inertia/r) +k*(m+1)* log(r))


def bic_k_best(data, clustering, cod):
    center=np.loadtxt(open(cod, "r"), delimiter=" ", skiprows=1)
    inertia=0
    r,m=data.shape
    for idx, vect in enumerate(data):
        dist=minkowski(vect,center[clustering[idx]],1)
        inertia+=dist *  dist
    k,m=center.shape
    return (r*log(inertia/r) +k*(m+1)* log(r))


data_dir="data"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]

for exp in data_dirs:
    if "R52" in exp or "R8" in exp:
        continue
    X = [join(exp,f) for f in listdir(exp) if ".nrm" in f]
    X= FileReader.read_dat(X[0]).toarray()
    cod = [join(exp,f) for f in listdir(exp) if ".cod" in f][0]
    elm = FileReader.read_elm([join(exp,f) for f in listdir(exp) if ".elm" in f][0])
    print(exp, len(set(elm)),bic_k_best(X, elm, cod))
    lowest_bic = np.infty
    dico_bic = dict()
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
        bic=bic_k(kmeansi, R,n_components, M)
        if n_components not in dico_bic or bic < dico_bic[n_components]:
            dico_bic[n_components]=bic
        if bic < lowest_bic:
            lowest_bic = bic
            n_best=n_components
    print (exp,lowest_bic, n_best)
