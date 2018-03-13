# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:35:35 2017

@author: AD-Rahat
"""

def  countNt(k, isDNA):
    
    length = len(k)
    
    a = c = g = t = u = 0

    for i in k:
        if i == 'A':
            a = a+1;
        elif i == 'C':
            c = c+1;
        elif i == 'G':
            g = g+1;
        elif i == 'T':
            t = t+1
        elif i == 'U':
            u = u+1
        
    if isDNA:
        print 'The nucleotide frequencies of DNA is: '
        print "A = ", str( (1.0*100*a) / length ), '%'
        print "C = ", str( (1.0*100*c) / length ), '%'
        print "G = ", str( (1.0*100*g) / length ), '%'
        print "T = ", str( (1.0*100*t) / length ), '%'
    else:
        print 'The nucleotide frequencies of RNA is: '
        print "A = ", str( (1.0*100*a) / length ), '%'
        print "C = ", str( (1.0*100*c) / length ), '%'
        print "G = ", str( (1.0*100*g) / length ), '%'
        print "U = ", str( (1.0*100*u) / length ), '%'
    
    return


#### calling portion
print("")
k = raw_input("Enter the DNA or RNA sequence: ")
isDNA = 0
if "T" in k:
    isDNA = 1;
countNt(k, isDNA)
