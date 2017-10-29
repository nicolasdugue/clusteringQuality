#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample
import numpy as np
from sklearn.cluster import KMeans
from Comparateur import Comparateur
import matplotlib.pyplot as plt

from ..code.ioreader import FileReader

def subsamp(taille, pct):
    val=int(taille * pct)
    liste=range(val)
    s1=sample(liste, val)
    s2=sample(liste, val)
    common=set(s1).intersection(set(s2))
    return (s1,s2,common)

data_dir="/home/dugue/Bureau/aa-PackNicoAPIN"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]
for exp in data_dirs:
    if "ZOO" in exp:
        X=FileReader.read_dat("/home/dugue/Bureau/aa-PackNicoAPIN/ZOO/NONoise/zooB-n.nrm").toarray()
    else:
        if "R52" in exp or "R8" in exp or "VRBF" in exp or "SOY" in exp or "PEN" in exp:
            continue
        X = [join(exp,f) for f in listdir(exp) if "nrm" in f]
        X=fr.read_dat(X[0]).toarray()
    if "IRIS" in exp:
        n_components_range = range(2, 10)
    elif "WINE" in exp:
        n_components_range = range(2, 10)
    elif "ZOO" in exp:
        n_components_range = range(2, 10)
    else:
        n_components_range = range(2, 10)
    sim=[]
    R,M=X.shape
    for k in n_components_range:
        sim.append([])
        for i in range(100):
            #TODO Subsamp
            s1,s2,common=subsamp(R,0.8)
            clu1=KMeans(n_clusters=k, init='random', n_init=200).fit([X[i] for i in s1])
            clu2=KMeans(n_clusters=k, init='random', n_init=200).fit([X[i] for i in s2])
            #Use only common points
            test=Comparateur([clu1.labels_[i] for i in common], [clu2.labels_[i] for i in common])
            sim[k-2].append(test.get_correlation())
    for k in n_components_range:
        plt.figure()
        axes=plt.gca()
        axes.set_xlim([0,1])
        plt.hist(sim[k-2], bins='auto')
        split=exp.split("/")
        plt.savefig(split[len(split) -1]+"_"+str(k)+".png")
