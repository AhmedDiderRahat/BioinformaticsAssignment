# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:12:19 2017

@author: AD-Rahat
"""

def breakPoint(sequence):
    count = 0
    for i in range (0, len(sequence)-1):
        if abs(sequence[i]-sequence[i+1]) > 1: 
            count = count+1
    return count
    
def sortByReversal(sequence):
    print     
    print sequence        
    k=0
    
    while(True):
        if sorted(sequence) == sequence:
            break
        count = 0
        list = []
        for i in range (0, len(sequence)-1):
            if abs(sequence[i]-sequence[i+1]) > 1: 
                count = count+1
                list.append(i)
        if k == 0:
            print 'Break Point: ', str(count)
        k = k+1
  
        for i in range (1, len(list)):
            e = list[i]
            s = list[i-1] + 1
            temp = sequence[s:e+1]
            temp.reverse()
            temp2 = sequence[:s] + temp + sequence[e+1:]
            
            #print list

            if breakPoint(temp2) <= count:           
                sequence = temp2
                print sequence
                count = breakPoint(temp2)
                print 'Break Point: ', str(count)
        
        if k==100:
            break

temp = [1, 6, 7, 2, 3, 4, 5, 8]

sortByReversal(temp)