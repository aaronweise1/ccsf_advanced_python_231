# -*- coding: utf-8 -*-
"""
Created on Feb 15 2020

@author: Mary Liu
"""
import math
print (*map(lambda x: ' ' * int(math.sin(x)*math.pi + 10) + '~', range(20)), sep="\n")
