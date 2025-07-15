#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 14:16:39 2025

@author: patrickilunga
"""

import os
import segyio
import numpy as np
import matplotlib.pyplot as plt


# Chemin vers ton fichier SEGY (on commence par le plus petit)
# filename = "data/raw/SEAM_Interpretation_Challenge_1_2DSparseGathers_Depth.sgy"
filename = "/Users/patrickilunga/seam_project/data/raw/SEAM_Interpretation_Challenge_1_2DSparseGathers_Depth.sgy"

# Ouvre le fichier en mode lecture
with segyio.open(filename, "r", ignore_geometry=True) as f:
    # Lis la première trace (index 0)
    trace = f.trace[0]

    # Affiche quelques informations
    print(f"Nombre d'échantillons dans la trace : {len(trace)}")
    print(f"Quelques premières valeurs : {trace[:10]}")

    # Affiche la trace avec matplotlib
    plt.figure(figsize=(10, 4))
    plt.plot(trace)
    plt.title("Première trace sismique (SEGY)")
    plt.xlabel("Échantillon")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    # Sauvegarde la figure
    # plt.savefig("results/example_seismic_trace.png")  
    plt.show()
    

# Ouvre le fichier en mode lecture
with segyio.open(filename, "r", ignore_geometry=True) as f:
    # Lis la première trace (index 0)
    trace2 = f.trace.raw[:5]