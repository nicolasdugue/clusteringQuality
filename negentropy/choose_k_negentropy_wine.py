#!/usr/bin/env python
# -*- coding: utf-8 -*-

import quality as q
#import numpy lib using np namespace
import numpy as np

import sys
sys.path.append("common/ioreader")
import FileReader as fr

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    filename='debug_wine.log')
logger = logging.getLogger("Main")

from os import listdir
from os.path import isfile, join

mypath="../data/real/Wine-Kmeans/UCI_Wine/results/WineIGKMGN-NOPR/CLASSES/"
only_elm_files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and ".elm" in f]

matrix=fr.read_dat("/home/dugue/Test-Qual/UCI_Wine/results/wineO.dat")
min=0
nb=0
file_best=""
for f in only_elm_files:
    clustering=fr.read_elm(f)
    nb_elements=len(set(clustering))
    print("Nb elements in ", f," : ", nb_elements)
    obj=q.quality(matrix, clustering)
    try:
        neg=obj.get_negentropy_us()
        print(neg)
    except:
        continue
    if neg != -np.inf and neg < min:
        min=neg
        nb=nb_elements
        file_best=f
print("Best : ", min, nb, file_best)
