#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:43:27 2023

@author: pablo
"""

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("leb_oro.csv").sort_values(by='PT',ascending= False)

datos = data['PT']
etiquetas = data['Equipo']

fig, ax = plt.subplots()
ax.bar(etiquetas, datos)
ax.set_xticklabels(etiquetas, rotation=90)
ax.set_ylim([60, 85])

plt.show()


