# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 03:03:06 2017

@author: AD-Rahat
"""

dictionary = {}
output = []

def outputMethod(DNA, length):
    count = 0
    for i in range(0, len(DNA)-(length-1)):
        temp = DNA[i:length+i]
        if temp in dictionary:
            value = dictionary[temp]
            value = value + 1
            dictionary[temp] = value
            
        else:
            dictionary[temp] = 1
            output.insert(count, temp)
            count = count+1
    
    print '\nOutput is: \n'
    for temp in output:
        print temp, ' ', dictionary[temp]

DNA = raw_input("Enter the DNA sequence: ")
length = int(raw_input("\nEnter the length: "))

outputMethod(DNA, length)