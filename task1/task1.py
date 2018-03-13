# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:59:46 2017

@author: AD-Rahat
"""

from random import randint
import numpy as np

def genRandDNA(k):
    
    DNA_element = np.chararray((1, 4))
    DNA_element = [['A'], ['G'], ['C'], ['T']]
    
    outPut = ""
    temp = ""   
    
    for i in range (0,k):
        temp = ''.join(DNA_element[randint(0,3)])
        outPut = outPut + temp
    
    return outPut

#### calling portion
print("")
k = int(raw_input("Enter the length of the DNA: "))
answer =  genRandDNA(k)
print "The DNA sequence is: "
print answer