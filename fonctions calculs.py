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

def covariance(Liste_x, Liste_y, Moy_x, Moy_y):
    Resultat = 0
    L=len(Liste_x)
    for i in range(L):
        resultat += (Liste_x[i]-Moy_x)*(Liste_y[i]-Moy_y)
    Resultat=Resultat/L
    return Resultat

def correlation(Liste_x, Liste_y, Moy_x, Moy_y):
    ecarttype_x=ecarttype(Liste_x, Moy_x)
    ecarttype_y=ecarttype(Liste_y, Moy_y)
    if ecarttype_x==0: ecarttype_x = 1/1000000000
    if ecarttype_y==0: ecarttype_y = 1/1000000000
    return covariance(Liste_x, Liste_y, Moy_x, Moy_y)*1/(ecarttype_x*ecarttype_y)
