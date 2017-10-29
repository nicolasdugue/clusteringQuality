#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import cluster
import numpy as np
import itertools

from scipy import linalg
import sklearn.datasets
from sklearn import mixture

import sys
sys.path.append("common/ioreader")
import FileReader


data_dir="data"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]

for exp in data_dirs:
    if "R52" in exp or "R8" in exp:
        continue
    X = [join(exp,f) for f in listdir(exp) if "nrm" in f]
    X=FileReader.read_dat(X[0]).toarray()
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
    lowest_bic = np.infty
    dico_bic = dict()
    n_best=0
    n_components_range = range(1, 10)
    for n_components in n_components_range:
        # Fit a Gaussian mixture with EM
        gmm = mixture.GaussianMixture(n_components=n_components, n_init=50)
        gmm.fit(X)
        bic=gmm.bic(X)
        if n_components not in dico_bic or bic < dico_bic[n_components]:
            dico_bic[n_components]=bic
        if bic < lowest_bic:
            lowest_bic = bic
            best_gmm = gmm
            n_best=n_components
    print (exp,lowest_bic, n_best)
