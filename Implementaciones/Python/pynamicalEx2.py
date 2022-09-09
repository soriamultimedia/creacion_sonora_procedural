
#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Diagramas fase y de bifurcación para mapeo cúbico.
# https://github.com/gboeing/pynamical

import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pynamical import simulate, cubic_map, singer_map, bifurcation_plot, phase_diagram, phase_diagram_3d


#mapeo cúbico. Parámetros para distintas simulaciones. Iteraciones, rate_min, rate_max, num_rates
gens_bif = [100, 250, 600]
gens_phs = [1000, 1300, 3000]

rate_bif = [[1,4],[2,4],[1.5,4]]
rate_phs = [3.99, 3.99, 3.5]


n_rates_bif = np.full(4,1000)
n_rates_phs = [1,1,30]

#generar órbitas del mapeo para las conidiciones iniciales dadas
cubic_store_bif = [simulate(model=cubic_map, num_gens=gens,rate_min=rate[0], rate_max=rate[1], 
                 num_rates = num, 
                 num_discard = 100) for gens, rate, num in zip(gens_bif,rate_bif,n_rates_bif)]

cubic_store_phs = [simulate(model=cubic_map, num_gens=gens,rate_min= rate, num_rates = num, 
                 num_discard = 100) for gens, rate, num in zip(gens_phs,rate_phs,n_rates_phs)]

#plotear diagramas de bifuración
for data in cubic_store_bif:
    bifurcation_plot(data, title='Cubic Map Bifurcation Diagram', 
                     xmin=1, xmax=4, save=False)


#plotear diagramas de fase 3D
for data in cubic_store_phs:
    phase_diagram_3d(data, xmin=-1, xmax=1, ymin=-1, ymax=1, 
                     zmin=-1, zmax=1, save=False, alpha=0.2, 
                     color='viridis',azim=330, 
                     title='Cubic Map 3D Phase Diagram')



#---------------------------------------------
#mapeo singer. Parámetros para distintas simulaciones. Iteraciones, rate_min, rate_max, num_rates

gens_ = [1000, 1500, 3000]
rate_ = [1.07, 1.07, 1.045]
num_rates_sin = [1,1,30]


singer_store_phs = [simulate(model=singer_map, 
                             num_gens = gens, 
                             rate_min = rate,
                             num_rates=num, 
                             num_discard=100) for gens, rate, num in zip(gens_,rate_,num_rates_sin)]
                    

for data in singer_store_phs:
    phase_diagram_3d(data, 
                     alpha =0.3,
                     color = 'viridis',
                     title='Singer Map 3D Phase Diagram', 
                     save=False)


