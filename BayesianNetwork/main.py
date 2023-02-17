"""
    Universidad del Valle de Guatemala
    José Rodrigo Barrera García
    20807
    Laboratorio 2 - Redes Bayesianas
"""

from BayesianClass import *

A = Node("A", [True, False])
B = Node("B", [True, False], [A])
C = Node("C", [True, False], [A])
D = Node("D", [True, False], [B, C])
E = Node("E", [True, False], [D])

A.add_cpt_entry((), {True: 0.5, False: 0.5})

B.add_cpt_entry((True,), {True: 0.1, False: 0.9})
B.add_cpt_entry((False,), {True: 0.5, False: 0.5})

C.add_cpt_entry((True,), {True: 0.8, False: 0.2})
C.add_cpt_entry((False,), {True: 0.2, False: 0.8})

D.add_cpt_entry((True, True), {True: 0.99, False: 0.01})
D.add_cpt_entry((True, False), {True: 0.9, False: 0.1})
D.add_cpt_entry((False, True), {True: 0.9, False: 0.1})
D.add_cpt_entry((False, False), {True: 0.0, False: 1.0})
E.add_cpt_entry((False, False), {True: 0.0, False: 1.0})

network = BayesianNetwork([A, B, C, D])

# Cálculo de la probabilidad conjunta de un evento

event = {
    "A": True,
    "B": False,
    "C": True,
    "D": True
}

#Dada una red bayesiana (según sea la definición de su preferencia), devuelve si esta está completamente descrita (boolean)
print("\n¿Está totalmente descrita?: ",network.describe())
#Dada una red bayesiana (según sea la definición de su preferencia), devuelve la representación compacta de la red bayesiana (string)
print(network.compact())
#Dada una red bayesiana (según sea la definición de su preferencia), devuelve los factores de la misma (hash maps / diccionarios / key-value)
print(network.network_elements())
#Dada una red bayesiana (según sea la definición de su preferencia), y una consulta (según sea la definición de su preferencia), devuelve el resultado del algoritmo de enumeración sobre dicha red y dicha consulta(float)
joint_prob = network.inference(event)
print("\nLa probabilidad conjunta del evento es: ", joint_prob,"\n")