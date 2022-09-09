
#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Distribuciones básicas de probabilidad III. 
#Distribución normal y beta


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import beta

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)

#histograma
plt.figure(0)
plt.hist(s, 20, normed=True)

# Plot la curva de distribución
mu = 5
sigma = 10
snd = norm(mu, std)
X = snd.rvs(100)

#plot pmf
x = np.linspace(-100, 100, 1000)
#plt.figure(2)
#plt.plot(x, snd.pdf(x))


#Distribución beta

a, b = 2.31, 0.627
X = beta(1, 3)

fig, ax = plt.subplots(1, 1)

x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='beta pdf')


