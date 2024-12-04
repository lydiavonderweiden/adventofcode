import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Auslesen des gegebenen Feld der Risiken
    field = np.genfromtxt("test.txt", delimiter=1)
    #Initalisiert Feld der gefundenen Risiken auf den Weg
    risk = np.full_like(field, np.inf)
    #Tupel des Standort, initalisiert auf links oben
    ort = (0,0)

    ziel =( np.size(field, 0)-1, np.size(field, 1)-1)
    
    while ort != ziel:
        
    
    
    