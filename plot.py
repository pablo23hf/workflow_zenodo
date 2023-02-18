#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:43:27 2023

@author: pablo
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("leb_oro.csv").sort_values(by='PT',ascending= False)"

plt.ylim([65, 85])
plt.bar(data['Equipo'], data['PT'])

plt.xticks(data['Equipo'], rotation=90)

