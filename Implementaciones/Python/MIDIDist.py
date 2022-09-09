#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Transducción de distribución de probabilidad a notas. 

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import beta
from scipy.stats import poisson
from scipy.stats import geom
from scipy.stats import binom
from numpy import random
import string
import seaborn as sns
from sklearn.preprocessing import minmax_scale



#Alturas mediante distribución Poisson
#División por registros. Distribución diferente para cada registro.


#dist_type, args_dist = [values...], args_scale = [min, max]
def data_out(dist_type, *args_dist,scale_lim=[]):
    
    dist = {
        'poisson' : poisson.rvs(*args_dist),
        'binomial': binom.rvs(*args_dist),
        'geometric': geom.rvs(*args_dist),
        'beta' :   beta.rvs(*args_dist)
        }
    
    select = dist[dist_type]
   # return minmax_scale(select,feature_range=(scale_lim[0], scale_lim[1]))
 

low_pitch = minmax_scale(poisson.rvs(mu=3, size=300), feature_range=(10,30))
midLow_pitch = minmax_scale(poisson.rvs(mu=4, size=300), feature_range=(30,50))
midHigh_pitch = minmax_scale(poisson.rvs(mu=5.5, size=300), feature_range=(50,75))
highLow_pitch = minmax_scale(poisson.rvs(mu=2.5, size=300), feature_range=(75,95))
high_pitch = minmax_scale(poisson.rvs(mu=1.5, size=300), feature_range=(95,120))



#--------------------------------------------
#plot de histogramas de todos los muestreos

pitch = [low_pitch, midLow_pitch, midHigh_pitch, highLow_pitch, high_pitch]
labels=list(string.ascii_lowercase)[:len(pitch)]

def plot_mid(data, labels):
    fig = plt.figure()
    for i in data:
        sns.kdeplot(i)
    fig.legend(labels)


plot_mid(pitch, labels)
#duraciones mediante distribución geométrica
dur = minmax_scale(geom.rvs(0.5, size=300), feature_range=(0.1,1))


