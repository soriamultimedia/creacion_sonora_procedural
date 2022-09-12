# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:56:45 2022

@author: esori
"""


#Principios de creación sonora procedural.
#Permutaciones simples

from itertools import permutations
import numpy as np
import string
import matplotlib.pyplot as plt

#array con todas las permutaciones de un conjunto dado
base = np.arange(1,8)
perm = permutations(base)
prm_list = list(perm)

#permutaciones de k en n
perm = list(permutations(base, 3))
perm = list(permutations(base, 2))
perm = list(permutations(base, 5))

#con símbolos
alphbt = list(string.ascii_lowercase)
alph_0 = alphbt[:6]
perm = list(permutations(base, 3))

#alturas
pitch = list(string.ascii_uppercase)[:7]
perm = list(permutations(base, 4))

#permutaciones que tienen una nota en una posición específica
perm_pos = lambda perm_list, position, pitch: [i for i in perm_list if i[position] == pitch]

perm_pos(perm,0,'F')
perm_pos(perm,1,'C')


