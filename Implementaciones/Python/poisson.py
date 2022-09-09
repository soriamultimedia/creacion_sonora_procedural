
#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Distribuciones básicas de probabilidad II. Distribución de Poisson y geométrica.

import numpy as np
from numpy import random
from scipy.stats import poisson
from scipy.stats import geom
import matplotlib.pyplot as plt
import seaborn as sns


#mu/lambda (la proporción o media de éxitos observados durante un periodo de tiempo)
X = random.poisson(lam=2, size=1000)
X = poisson.rvs(mu=3, size=10000)

#plot histograma
plt.figure(0)
plt.hist(X, density=True, edgecolor='red')

#pmf --Probabilidad de obtener k éxitos durante un intervalo de tiempo. 
poisson.pmf(k=5, mu=3)
poisson.pmf(k=10, mu=6)

plt.figure(1)
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')


#cmdf (función de distribución acumulada)
poisson.cdf(k=3, mu=9)
poisson.cdf(k=12, mu=19)

#----------------------------------------------------------------------------
#Distribución geométrica
X = geom.rvs(0.5, size=10000)
X = np.random.geometric(0.65, 1000)

#histograma
bin = np.arange(0,20,1)

plt.figure(2)
plt.hist(X, bins=bin, edgecolor='blue') 
plt.title("Geometric Distribution")

#pmf calculando eventos por función quantil
p = 0.1
q = np.arange(geom.ppf(0.01, p), geom.ppf(0.99, p))

fig, ax = plt.subplots(1, 1)
ax.plot(q, geom.pmf(q, p), 'bo', ms=8, label='geom pmf')
ax.vlines(q, 0, geom.pmf(q, p), colors='b', lw=5, alpha=0.5)



