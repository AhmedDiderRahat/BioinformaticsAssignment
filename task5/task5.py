# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:02:41 2017

@author: AD-Rahat
"""

def convDNAtoRNA(DNA):

    output = ""

    for i in DNA:
        if i == 'T':
            output = output + 'U'
        else:
            output = output + i
    
    return output

#### calling portion
print("")
DNA = raw_input("Enter the DNA sequence: ")
ans = convDNAtoRNA(DNA)
print ans
