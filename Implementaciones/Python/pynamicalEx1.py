
#Principios básicos de creación Sonora Procedural. Edmar Soria.
#Diagramas fase y de bifurcación para ecuación logística.
# https://github.com/gboeing/pynamical

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pynamical
from pynamical import simulate, bifurcation_plot, save_fig,  phase_diagram, phase_diagram_3d



title_font = pynamical.get_title_font()
label_font = pynamical.get_label_font()

#Función para generar órbitas de la ecuación logística. Num_gens--número de iteraciones,
#rate min/max--- es el intervalo del parámetro de control de la ecuación
#num rates---- es lel número de órbitas para conidicones inciales específicas. 
#Por ejemplo, rate_min=0, rate_max=4 y num_rates=1000
#significará que se realizarán 1000 simulaciones para 1000 C.I. distintas diviendo precisamente el
#intervalo [0,4] en 1000 partes iguales, en donde cada parte corresponderá a una C.I.
#para un valor del paráemtro de control.


#ploteo del diagrama de bifurcación

pops = simulate(num_gens=100, rate_min=0, rate_max=4, num_rates=1000)
bifurcation_plot(pops, filename='logistic-map-bifurcation-0')

pops = simulate(num_gens=100, rate_min=2.8, rate_max=4, num_rates=1000, num_discard=200, initial_pop=0.1)
bifurcation_plot(pops, xmin=2.8, xmax=4, filename='logistic-map-bifurcation-2')

pops = simulate(num_gens=100, rate_min=3.7, rate_max=3.9, num_rates=1000, num_discard=100)
bifurcation_plot(pops, xmin=3.7, xmax=3.9, filename='logistic-map-bifurcation-3')

pops = simulate(num_gens=200, rate_min=3.84, rate_max=3.856, num_rates=1000, num_discard=300)
bifurcation_plot(pops, xmin=3.84, xmax=3.856, ymin=0.445, ymax=0.552, filename='logistic-map-bifurcation-4')


title_font = pynamical.get_title_font()
label_font = pynamical.get_label_font()


#ploteo del diagrama/mapa de fase.
pops = simulate(num_gens=100, rate_min=3.5, num_rates=1, num_discard=100)
phase_diagram(pops, title='Logistic Map Attractor, r=3.5', size=20)

pops = simulate(num_gens=2000, rate_min=3.9, num_rates=1)
phase_diagram(pops, xmin=0.25, xmax=0.75, ymin=0.8, ymax=1.01, size=20, title='Logistic Map Attractor, r=3.9')

pops = simulate(num_gens=2000, rate_min=3.6, rate_max=4.0, num_rates=50)
phase_diagram(pops, xmin=0.25, xmax=0.75, ymin=0.8, ymax=1.01, size=7, 
              title='Logistic Map Attractor, r=3.6 to r=4.0', color='viridis')

pops = simulate(num_gens=4000, rate_min=3.6, rate_max=4.0, num_rates=50)
phase_diagram_3d(pops, title='Logistic Map Attractor, r=3.6 to r=4.0', alpha=0.1, color='viridis', color_reverse=False, 
                 azim=230, filename='3d-logistic-map-attractor-1')

phase_diagram_3d(pops, title='Logistic Map Attractor, r=3.6 to r=4.0', alpha=0.1, color='viridis', color_reverse=False, 
                 elev=7, azim=320, filename='3d-logistic-map-attractor-2')
