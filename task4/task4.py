# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:54:58 2017

@author: AD-Rahat
"""

def getRevComplement(k, isDNA):

    complementarySeq = ""
    temp=""
    
    if isDNA:
        for i in k:
            if i == 'A':
                temp = ''.join('T')
            elif i == 'C':
                temp = ''.join('G')
            elif i == 'G':
                temp = ''.join('C')
            elif i == 'T':
                temp = ''.join('A')
            complementarySeq = complementarySeq + temp  
    else:
        for i in k:
            if i == 'A':
                temp = ''.join('U')
            elif i == 'C':
                temp = ''.join('G')
            elif i == 'G':
                temp = ''.join('C')
            elif i == 'U':
                temp = ''.join('A')
            complementarySeq = complementarySeq + temp
    return complementarySeq


#### calling portion
print("")
k = raw_input("Enter the DNA or RNA sequence: ")
isDNA = 0
if "T" in k:
    isDNA = 1;
ans = getRevComplement(k, isDNA)
print ans
