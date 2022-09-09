# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Distribuciones básicas de probabilidad I. 

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import binom
from numpy import random

#disribución binomial
#Definir variable aleatoria (de acuerdo al experimento a realizar) con valores
# n (número de ocurrencias del evento) y p (probabilidad de éxito del
#experimento Bernoulli)

#Distribución del número de veces que se puede obtener un 6 lanzando un dado
#100 veces.

n = 100
p = 1/6
X = binom(n, p)

#Distribución del número de caras que se pueden obtener lanzando una moneda
#800 veces.
n = 800
p = 1/2
X = binom(n, p)

#Obtener 300 muestreos de la distribución definida 
X.rvs(300);

#función de masa y función de distribución acumulada
X.pmf(5)
X.cdf(4)

#Lo mismo pero con numpy
X = random.binomial(n=100, p=1/6, size=100)
X = random.binomial(n=800, p=1/2, size=300)

#Obtener histograma con seaborn y matplot
plt.figure(0)
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.figure(1)
plt.hist(X)


#dejando fijo el sembrado (reproducibilidad)
np.random.seed(4)

size = 10000

X = np.random.binomial(20, 0.5, size)

#bin para histograma
bin = np.arange(0,20,1)

plt.figure(2)
plt.hist(X, bins=bin, edgecolor='red') 
plt.title("BDistribución binomial") 
plt.show()

#Obtener estadísticas básicas de la distribución
X.mean()
X.var()
X.std()

#plotear distintos histogramas de diferentes distribuciones
plt.figure(3)
sns.kdeplot(np.random.binomial(150, 0.3, size))

plt.figure(4)
sns.kdeplot(np.random.binomial(200, 0.1, size))

plt.figure(5)
sns.kdeplot(np.random.binomial(550, 0.7, size))


#función de masa de probabilidad
#n (número de veces que es realizado el experimento), p (probabilidad
#de éxito del experimento Bernoulli), r (valores de la VA, número de éxitos)

n = 100
p = 0.2
r_values = list(range(n + 1))

#calcular la pmf para cada valor de la VA
dist = [binom.pmf(r, n, p) for r in r_values ]

#media/varianza y plot
mean, var = binom.stats(n, p)

plt.figure(6)
sns.kdeplot(dist)


