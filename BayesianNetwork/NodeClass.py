"""
    Universidad del Valle de Guatemala
    José Rodrigo Barrera García
    20807
    Laboratorio 2 - Redes Bayesianas
"""

class Node(object):
    # Inicializar los atributos del objeto directamente y establecer parents y cpt en una lista vacía y un diccionario vacío, respectivamente, si no se proporcionan.
    def __init__(self, name, states, parents=None, cpt=None):
        self.name = name
        self.states = states
        self.parents = parents or []
        self.cpt = cpt or {}
        
    # Agregar un padre a la lista de padres
    def add_parent(self, parent):
        self.parents.append(parent)
        
    # Agregar una entrada al diccionario de cpt
    def add_cpt_entry(self, entry, value):
        self.cpt[entry] = value
    
    # Devolver una cadena de texto que representa el objeto Node y su información asociada utilizando f-strings para formatear la cadena
    def __str__(self):
        return f"P({self.name}): {self.cpt}\nParents: {[node.name for node in self.parents]}\n"


        