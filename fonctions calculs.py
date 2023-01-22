from math import sqrt


def pourcentage(x,y):
    return x/(y/100)

def moyenne(Liste):
    total=0
    for element in Liste:
        total += element
    return total/len(Liste)


def ecarttype(Liste, Moy):
    variance=0
    for element in Liste:
        variance += (element-Moy)**2
    variance=variance/len(Liste)
    return sqrt(variance)

def covariance(Liste1, Liste2, Moy1, Moy2):
    Resultat = 0
    L=len(Liste1)
    for i in range(L):
        resultat += (Liste1[i]-Moy1)*(Liste2[i]-Moy2)
    Resultat=Resultat/L
    return Resultat

def correlation(Liste1, Liste2, Moy1, Moy2):
    ecarttype1=ecarttype(Liste1, Moy1)
    ecarttype2=ecarttype(Liste2, Moy2)
    if ecarttype1==0: ecarttype1 = 1/1000000000
    if ecarttype2==0: ecarttype2 = 1/1000000000
    return covariance(Liste1, Liste2, Moy1, Moy2)*1/(ecarttype1*ecarttype2)
