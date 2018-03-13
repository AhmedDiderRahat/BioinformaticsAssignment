# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:41:40 2017

@author: AD-Rahat
"""

dictionary = {}
output = []

def outputMethod(DNA, length):
    count = 0
    for i in range(0, len(DNA)-(length-1)):
        temp = DNA[i:length+i]
        if temp not in dictionary:
            dictionary[temp] = 1
            output.insert(count, temp)
            count = count+1
    
    print '\nOutput is: \n'
    for temp in output:
        print temp

DNA = raw_input("Enter the DNA sequence: ")
length = int(raw_input("\nEnter the length: "))

outputMethod(DNA, length)