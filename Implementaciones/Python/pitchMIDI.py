
#Principios de creación sonora procedural. 
#Generación de parámetros sonoros mediante distribuciones de probabilidad y 
#exportación para archivo MIDI

#definir funcionesy diccionario para 
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import string
import seaborn as sns
from sklearn.preprocessing import minmax_scale
from midiutil import MIDIFile

def binom_s(*args_dist):
    return random.binomial(*args_dist)
    
def poisson_s(*args_dist):
    return random.poisson(*args_dist)

def geometric(*args_dist):
    return random.geometric(*args_dist)

def beta(*args_dist):
    return random.beta(*args_dist)
    
def normal(*args_dist):
    return random.normal(*args_dist)


def dict_set(funcs_):
    names = [i.__name__ for i in funcs]
    out = { names[i] : funcs[i] for i in range(0, len(names) ) }
    return out

#Array de funciones y definición de diccionarios
funcs = [binom_s, poisson_s, geometric, beta, normal]
dist_dic = dict_set(funcs)

#(tipo de distribución,escala mínimo, escala máximo, args.. de la distribución
def data_dist(dist_type,a,b, *args):
    out = dist_dic[dist_type](*args)
    out = minmax_scale(out,feature_range=(a,b))
    return out

#función para convertir nombres de variables en strings. Amr Sharaki:
#https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string

def getVariableNames(variable):
    results = []
    globalVariables=globals().copy()
    for globalVariable in globalVariables:
        if id(variable) == id(globalVariables[globalVariable]):
            results.append(globalVariable)
    return results   

#----------------------------------------------------------------------------

#generar datos para alturas con distribución de poisson
#definir diversos registros de alturas con el escalador
#altura y velocity deben ser int
data_size = 300

low_pitch = data_dist('poisson_s', 10,30, *[3,data_size])
midLow_pitch = data_dist('poisson_s', 30,50, *[3,data_size])
midHigh_pitch = data_dist('poisson_s', 50,75, *[5.5,data_size])
highLow_pitch = data_dist('poisson_s', 75,90, *[2.5,data_size])
high_pitch = data_dist('poisson_s', 95,120, *[1.5,data_size])

pitch_data = [low_pitch, midLow_pitch, midHigh_pitch, highLow_pitch, high_pitch]
pitch_labels = [getVariableNames(i)[0] for i in pitch_data]
pitch_data_int = [item.astype(int) for item in pitch_data]
marks = len(pitch_data)
#plot de histogramas de todos los muestreos
def plot_mid(data, labels):
    fig = plt.figure()
    for i in data:
        sns.kdeplot(i)
    fig.legend(labels)

plot_mid(pitch_data, pitch_labels)

#-----------------------------------------------------------------
#generar datos para duraciones de notas con distribución normal
durs = [[0.2,0.5],[0.15,0.4],[0.1,0.3],[0.05,0.2],[0.05,0.1],[0.05,0.15]]

val = lambda a,b,n : random.randint(a,b,n)
bin_params = [[i,j,w] for i,j,w in zip(val(100,200,5),val(1,80,5)*0.01,np.full(marks,data_size))]


#duraciones en list comprehension
durs_data = [data_dist('binom_s', a,b, *c) for [a,b],c in zip(durs,bin_params)]
#etiquetas para duraciones
durs_labels = list(string.ascii_lowercase)[:len(durs_data)]
#durs_data_int = [item.astype(int) for item in durs_data]

#plot de histogramas de las duraciones para cada registro

plot_mid(durs_data, durs_labels)


#---------------------------------------------------------------------
#data de velocity reciclando las duraciones
vel_data = np.floor(minmax_scale(durs_data, feature_range=(30,110)))
vel_data = vel_data.astype(int)

#data de tiempo (posición de cada nota) reciclando duraciones
time = [np.arange(1,data_size+1,1) for i in range(marks)]
time_s = minmax_scale(durs_data, feature_range=(0.01,0.3))
time_data = [np.sort(a+b) for a,b in zip(time,time_s)]
#time_data = [item.astype(int) for item in time_data]

#track, *canal, time(base notas), tempo. Track por cada registro
track_data = [[i+1,0.5,80] for i in range(marks)]


#---------------------------------------------------------------------
# función para generar archivos midi de cada track
def arm_track(track_info, pitch_info, time_info, dur_info, vel_info, path, name):
    size_tracks = len(track_info)
    distMIDI = [MIDIFile(i+1) for i in range(size_tracks)] 
    
    for midiTrack,j in zip(distMIDI, track_info):
        midiTrack.addTempo(*j)  
        
    for i in range(size_tracks):
        for pitch, time, dur, vel in zip(pitch_info[i], time_info[i], dur_info[i], vel_info[i]):
            distMIDI[i].addNote(i,0,pitch, time, dur, vel)
            
    for i in range(marks):
         with open(path+name+f'_{i}.mid', "wb") as output_file:
            distMIDI[i].writeFile(output_file) 

path = '/Users/soria/Downloads/'
name = 'track'
#midiFiles = arm_track(track_data, pitch_data_int, time_data, durs_data, vel_data,path,name)
    
    
