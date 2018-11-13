# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:26:20 2017

@author: AD-Rahat
"""

def countTwoMer(k):
    
    unique = {}
    
    print '\n\nTwo Mer Count ... ... ...'

    length = len(k)
    
    for i in range (0, length-(1)):
        temp = k[i:i+2]
        if temp in unique:
            value = unique[temp] + 1
            unique[temp] = value
        else:
            unique[temp] = 1
    
    totalNumberofTwoMer = 0
    for key in unique:
        totalNumberofTwoMer = totalNumberofTwoMer + unique[key]
    
    print totalNumberofTwoMer
    
       
    for key in unique:
        value = unique[key]
        percantage = (value * 1.0 * 100) / (totalNumberofTwoMer)
        print key, ' ', percantage
    
    return
    
def  countOneMer(k):
    
    length = len(k)    
    a = c = g = t = 0
    for i in k:
        if i == 'A':
            a = a+1;
        elif i == 'C':
            c = c+1;
        elif i == 'G':
            g = g+1;
        elif i == 'T':
            t = t+1
        
    print '\nThe One Mer frequencies of DNA is: '
    print "A = ", str( (1.0*100*a) / length ), '%'
    print "T = ", str( (1.0*100*t) / length ), '%'
    print "C = ", str( (1.0*100*c) / length ), '%'
    print "G = ", str( (1.0*100*g) / length ), '%'
  
    return


#### calling portion
print("")
k = raw_input("Enter the DNA sequence: ")
countOneMer(k)
countTwoMer(k)

