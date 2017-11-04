#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import quality as q
#import numpy lib using np namespace
import numpy as np

import sys
sys.path.append("common/ioreader")
import FileReader

from os import listdir
from os.path import isfile, join

mypath="data"
only_elm_files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and ".elm" in f]


data_dir="data"
from os import listdir
from os.path import isfile, join
data_dirs = [join(data_dir,f) for f in listdir(data_dir) if not(isfile(join(data_dir, f)))]


for exp in data_dirs:
    if "Pen" in exp:
        min=0
        nb=0
        file_best=""
        X = [join(exp,f) for f in listdir(exp) if ".nrm" in f]
        X=FileReader.read_dat(X[0]).toarray()
        elms = [join(exp,f) for f in listdir(exp) if ".elm" in f]
        for elm in elms:
            clustering=FileReader.read_elm(elm)
            nb_elements=len(set(clustering))
            obj=q.quality(X, clustering)
            try:
                neg=obj.get_negentropy_us()
                print(exp, neg, nb_elements)
            except:
                continue
            if neg != -np.inf and neg < min:
                min=neg
                nb=nb_elements
                file_best=elm
        print(exp,"Best : ", min, nb, file_best)
