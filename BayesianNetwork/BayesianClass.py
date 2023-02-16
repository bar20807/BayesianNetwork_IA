"""
    Universidad del Valle de Guatemala
    José Rodrigo Barrera García
    20807
    Laboratorio 2 - Redes Bayesianas
"""

from NodeClass import *

class BayesianNetwork(object):
    def __init__(self, network):
        self.network = network
        self.probabilities = 1
        self.network_result = {}

    def describe(self):
        # Si existe algún estado en la red que no está presente en la tabla de probabilidad condicional (CPT) de su padre, devuelve False. En caso contrario, devuelve True.
        if not all(state in set(node.cpt[parent_states]) for node in self.network for parent_states in node.cpt for state in node.states):
            return False

        
    def compact(self):
        # Crear una lista de cadenas que contengan información sobre cada nodo en la red bayesiana
        node_strings = [str(node) + "\n" for node in self.network]
        # Concatenar las cadenas en una sola cadena utilizando el método join()
        return "".join(node_strings)

        
    def network_elements(self):
        # Crear un diccionario donde las claves son los nombres de los nodos y los valores son los CPT correspondientes
        # Utilizar una comprensión de diccionario para iterar sobre cada nodo en self.network y crear automáticamente la entrada correspondiente en el diccionario resultante
        return {node.name: node.cpt for node in self.network}


    def inference(self, query):
        # Crear una lista de tuplas que contengan los estados de los padres para cada nodo en la red bayesiana
        parent_states_list = [tuple([query[parent.name] for parent in node.parents]) for node in self.network]
        # Iterar sobre cada nodo en la red bayesiana
        for i, node in enumerate(self.network):
            # Obtener el estado del nodo actual a partir de la consulta
            node_state = query[node.name]
            # Obtener el valor de CPT correspondiente a los estados de los padres y el estado del nodo actual
            # Si no hay un valor de CPT correspondiente a los estados de los padres, utilizar el valor correspondiente al estado del nodo actual solamente
            cpt_value = node.cpt.get(parent_states_list[i], {}).get(node_state, 1)
            # Multiplicar el valor de CPT al producto acumulado de probabilidades
            self.probabilities *= cpt_value

        # Devolver el producto acumulado de probabilidades
        return self.probabilities

        
        