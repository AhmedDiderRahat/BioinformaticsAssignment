# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:18:20 2017

@author: AD-Rahat
"""

def complement(k):

    complementarySeq = ""
    temp=""
    
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
    return complementarySeq


#### calling function
print("")
k = raw_input("Enter the DNA or RNA sequence: ")
ans = complement(k)
print "The Complementary Stand is : ", ans
