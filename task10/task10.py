# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:17:16 2017

@author: AD-Rahat
"""

def numberMutation(sequence1, sequence2):
    count = 0
    for i in range(0, len(sequence1)):
        if sequence1[i] != sequence2[i]:
            count = count + 1
            
    print '\nNumber of Mutation: ', count      
    
numberMutation('AGTCGGAAC', 'CGTCGGCCC')