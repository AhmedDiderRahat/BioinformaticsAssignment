# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 01:13:32 2017

@author: AD-Rahat
"""

def dotMAtrixCreate(s1, s2):
    print
    print s1, s2
    dotMatrix = []
    for i in range(0, len(s1)):
        raw = []
        for j in range (0, len(s2)):
            raw.append('#')
        dotMatrix.append(raw)

    for i in range(0, len(s1)):
        raw = []
        for j in range (0, len(s2)):
            if s1[i] == s2[j]:
                dotMatrix[i][j] = 'O'
                
        
    for i in range(0, len(s1)):        
        for j in range (0, len(s2)):
            print dotMatrix[i][j],
        print 
 
s1 = 'AATGGTCCTCT'
s2 = 'CATGGTCGGCTCT'
dotMAtrixCreate(s1, s2)