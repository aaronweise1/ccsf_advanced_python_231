#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 2
# Due date  :  February 16, 2020
# Filename: hw2.py

"""
Write a program one statement long that displays the curvature of a sinusoid on the terminal
"""
import math
print(*map(lambda n: '-'*int(20+20*math.cos(n*.2)) + '*', range(90)), sep= '\n')