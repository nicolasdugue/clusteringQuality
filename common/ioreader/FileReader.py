#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.sparse import coo_matrix
import numpy as np

def read_elm(file_path):
    fichier=open(file_path)
    cpt=0
    clustering=[]
    for ligne in fichier:
        if cpt != 0:
            cluster=int(ligne.split(" ")[0])
            clustering.append(cluster)
        else:
            cpt+=1
    return clustering


# In python doc :
#>>> row  = np.array([0, 3, 1, 0])
#>>> col  = np.array([0, 3, 1, 2])
#>>> data = np.array([4, 5, 7, 9])
#>>> coo_matrix((data, (row, col)), shape=(4, 4)).toarray()
#array([[4, 0, 9, 0],
#       [0, 7, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 5]])

def read_dat(file_path):
    fichier=open(file_path)
    cpt=0
    nb_rows=0
    nb_cols=0
    row=[]
    col=[]
    data=[]
    for ligne in fichier:
        if cpt != 0:
            cpt_col=0
            data_ligne=ligne.split(" ")
            for i in data_ligne:
                if cpt_col < nb_cols:
                    i=float(i)
                    if i != 0:
                        data.append(i)
                        row.append(cpt - 1)
                        col.append(cpt_col)
                cpt_col+=1
        else:
            #First ligne = nb of cols
            nb_cols=int(ligne)
        cpt+=1
    nb_rows=cpt -1

    print(nb_rows)
    print(nb_cols)
    row  = np.array(row)
    col  = np.array(col)
    data = np.array(data)
    return coo_matrix((data, (row, col)), shape=(nb_rows, nb_cols))
