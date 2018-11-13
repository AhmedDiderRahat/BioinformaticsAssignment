# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:09:24 2017

@author: AD-Rahat
"""

def hammingDistance(sequence1, sequence2):
    count = 0
    for i in range(0, len(sequence1)):
        if sequence1[i] != sequence2[i]:
            count = count + 1
            
    print '\nHamming Distance: ', count      


#Calling Function
sequence1 = 'ATGCCC'
sequence2 = 'AUGCCT'
hammingDistance(sequence1, sequence2)
