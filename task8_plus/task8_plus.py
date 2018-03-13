# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 03:13:39 2017

@author: AD-Rahat
"""

from random import randint
import numpy as np
import codecs
def genRandDNA(k):
    
    fout = codecs.open("DNA_sequence.txt","w", encoding="UTF-8")    
    DNA_element = np.chararray((1, 4))
    DNA_element = [['A'], ['G'], ['C'], ['T']]
    
    for i in range (0,k):
        temp = ''.join(DNA_element[randint(0,3)])
        fout.write(temp)
    
    #return outPut
    fout.close()



def findSequence(k):   
    f_in = codecs.open("DNA_sequence.txt","r", encoding="UTF-8")
    for w in f_in:
        DNA = w.strip()
    f_in.close()
    
    dictionary = {}
    output = []
    count = 0
    #print '\n\n', DNA , '\n\n'
    for i in range(0, len(DNA)-(k-1)):
        temp = DNA[i:k+i]
        if temp in dictionary:
            value = dictionary[temp]
            value = value + 1
            dictionary[temp] = value
            
        else:
            dictionary[temp] = 1
            output.insert(count, temp)
            count = count+1

        
    fout = codecs.open("output.txt","w", encoding="UTF-8")    
    fout.write(DNA)
    fout.write('\n')
    for temp in output:
        fout.write(temp + ' ' + str(dictionary[temp]))
        fout.write('\n')
    fout.close()



"""
@Main Algorithm Start
"""
dnaLength = 100000
sequenceLength = 10
genRandDNA(dnaLength)

findSequence(sequenceLength)

#print ans

                
