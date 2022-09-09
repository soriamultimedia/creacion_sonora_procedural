
#Principios de creación sonora procedural. 
#Implementaciones básicas de Teoría de Grupos. 
#Ciclos, Permutaciones, Grupo Simétrico y Grupo Diédrico.
#https://docs.sympy.org/latest/index.html

from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics import Polyhedron
from sympy.combinatorics import Cycle, Permutation
from sympy import init_printing
import string
from sympy.combinatorics.named_groups import SymmetricGroup
import random
from sympy.combinatorics.named_groups import DihedralGroup
import itertools
init_printing(perm_cyclic=False, pretty_print=False)

#Permutaciones en forma de fila --> representación en ciclo
p = Permutation([0, 2, 1]);
q = Permutation([4,2, 1,3,0]);
r = Permutation([5,1,3,2,0,4])


#representación en fila a partir del ciclo
Permutation(1, 2)(1, 3)(2, 3)
[i^p for i in range(p.size)]
[i^q for i in range(q.size)]
[i^r for i in range(r.size)]


#multiplicaciones entre permutaciones
p = Permutation([0, 2, 1]);
q = Permutation([2, 0, 1]);
pq = Permutation([i^p*q for i in range(q.size)])
qp = Permutation([i^q*p for i in range(q.size)])
list(q*p)
list(p*q)

r = Permutation([5,1,3,2,0,4])
s = Permutation([3,1,5,2,4,0])
rs = Permutation([i^r*s for i in range(q.size)])
sr = Permutation([i^s*r for i in range(q.size)])
list(r*s)
list(s*r)

#expresión como biyección
q = Permutation([5, 2, 3, 4, 1, 0])
{i: q(i) for i in range(q.size)} 


p = Permutation([1, 0, 2, 3])
{i: p(i) for i in range(p.size)} 


#factorización mediante transposiciones

q.transpositions()
p.transpositions()
r.transpositions()
s.transpositions()

#-------------------------------------------------------------
#Grupos simétricos
G = SymmetricGroup(3)
G.order()
list(G.generate_schreier_sims(af=True))

H = SymmetricGroup(5)
H.order()
list(H.generate_schreier_sims(af=True))

#---------------------------------------------------------
#asociación con símbolos
D = ['ppp','pp','p','mf','f','ff']
card = len(D)
G = SymmetricGroup(card)
G_set = list(G.generate_schreier_sims(af=True))

#elegir una permutación de Sn y obtener su representación en dinámicas
p = Permutation(random.choice(G_set))
p(D)

#alturas
Pitch = list(string.ascii_uppercase)[:7]
for i in range(2):
    Pitch += [Pitch.pop(0)]

card_p = len(Pitch)
H = SymmetricGroup(card_p)
H_set = list(H.generate_schreier_sims(af=True))

#un conjunto aleatorio de 20 permutaciones
p_cycl = [Permutation(random.choice(H_set)) for i in range(20)]
p_set = [perm(Pitch) for perm in p_cycl]

#------------------------------------------------------------------------
#Grupos diédricos. Función que arroja las permutaciones en 3 representaciones
def Dh_n(n):
    Dh_ = DihedralGroup(n)
    perm_ = list(Dh_.generate_dimino())
    cycle = [perm.cyclic_form for perm in perm_]
    biy = [{i: q(i) for i in range(q.size)} for q in perm_]
    return perm_, cycle, biy

p_3, c_3, b_3 = Dh_n(3)
p_3, c_4, b_4 = Dh_n(4)

#Usando el grupo diédrico para secuencias de notas (u otros símbolos musicales)
#Definir un conjunto de notas aleatorias de cardinal dado y mostrar
#todas las permutaciones asociadas de acuerdo al grupo dihédrico corresponideinte

def dh_input(perm_base):
    size = len(list(perm_base))
    dh_perm = Dh_n(size)[0]
    dh_out = [perm(perm_base) for perm in dh_perm]
    return dh_out
    
pitch_base_1 = random.sample(Pitch,6)
pitch_base_2 = random.sample(Pitch,3)
pitch_base_3 = random.sample(Pitch,4)
p_base_D = [pitch_base_1 ,pitch_base_2, pitch_base_3]

dihedral_perms = [dh_input(i) for i in p_base_D]

#Ejemplo con escala cromática.
Sharp = [pitch+'#' for pitch in Pitch]
Chrom = list(itertools.chain.from_iterable(zip(Pitch,Sharp)))
del Chrom[5]
del Chrom[len(Chrom)-1]


#Formar el grupo diédrico D_12 para la escala cromática

p_12, c_12, b_12 = Dh_n(12)
x = p_12[0]
x(Chrom)

#Obtener todas las permutaciones de D_12 en términos de alturas
D_12Pitch = [item(Chrom) for item in p_12]

#Grupo diédrico D_6 para alturas
p_6, c_6, b_6 = Dh_n(6)
D_6Pitch = [item(Chrom) for item in p_6]

#Duraciones rítmicas
dur = np.geomspace(4, 0.25/2, num=6)
Dur = ['whole','half','♩', 'oct', 'sixt', 'thirt']
D_6Dur = [item(Dur) for item in p_6]

