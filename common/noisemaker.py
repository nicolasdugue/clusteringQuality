import random as rd

def random_noise(clustering, percentage, clu_max):
    cls=[]
    for idx, etiquette in enumerate(clustering):
        alea=rd.randint(0,100)
        if alea > (100 - percentage):
            cls.append(rd.randint(0,(clu_max - 1)))
        else:
            cls.append(clustering[idx])
    return cls
