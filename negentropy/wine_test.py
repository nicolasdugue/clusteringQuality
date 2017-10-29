#!/usr/bin/env python
# -*- coding: utf-8 -*-

import quality as q
#import numpy lib using np namespace
import numpy as np

import sys
sys.path.append("common/ioreader")
import FileReader as fr
sys.path.append("common")
import noisemaker as ns

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    filename='debug.log')
logger = logging.getLogger("Main")

clustering=fr.read_elm("/home/dugue/Test-Qual/UCI_Wine/results/wine_partition.elm")
nb_elements=len(set(clustering))
print("Nb elements : ", nb_elements)
matrix=fr.read_dat("/home/dugue/Test-Qual/UCI_Wine/results/wineO.dat")
obj=q.quality(matrix, clustering)
print(obj.get_negentropy_us())
for i in [10,30,50,90,100]:
    print("i : ",i)
    for k in range(10):
        cls=ns.random_noise(clustering,i,nb_elements)
        #print(cls)
        obj=q.quality(matrix, cls)
        print(obj.get_negentropy_us())
