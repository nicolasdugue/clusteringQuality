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
    #elif "R8" in exp:
    #    n_components_range = range(2, 25)
    else:
        n_components_range = range(2, 10)

    lowest_aic = np.infty
    dico_aic = dict()
    n_best=0
    for n_components in n_components_range:
        # Fit a Gaussian mixture with EM
        gmm = mixture.GaussianMixture(n_components=n_components, n_init=3)
        gmm.fit(X)
        aic=gmm.aic(X)
        if n_components not in dico_aic or aic < dico_aic[n_components]:
            dico_aic[n_components]=aic
        if aic < lowest_aic:
            lowest_aic = aic
            best_gmm = gmm
            n_best=n_components
    print (exp,lowest_aic, n_best)
