# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:55:09 2017

@author: AD-Rahat
"""

import codecs
import math
f_in = codecs.open("input.txt","r", encoding="UTF-8")
for w in f_in:
    delX = (w.strip()).split()
    
f_in.close()

length = len(delX)

a = 1.0
b = -1.0
c = -(2.0*length)
n1 = (-b + math.sqrt((b*b) - (4*a*c))) / (2.0*a)
n2 = (-b - math.sqrt((b*b) - (4*a*c))) / (2.0*a)

if n1>n2:
    n=n1
else:
    n=n2

output = []
output.insert(0, 0)
output.insert(1, int(delX[length-1]))
delX.pop(length-1)
count = 2
tempMap = 0


for i in range(0, 4):
    markElement = []
    mcount = 0
    zeros = [0 for x in range(length)]
    #print zeros[length-1]
    cnt = 0
    for j in range(0, len(output)):
        for k in range(0, len(delX)):            
            if (abs(int(delX[i])-int(output[j])) == int(delX[k])) and (zeros[k]==0):
                zeros[k] = 1
                cnt = cnt+1
                markElement.insert(mcount, k)
                mcount = mcount+1
                
    if cnt >= len(output):
        print output
        output.insert(count, int(delX[i]))
        output.sort()
        print output
        count = count+1
        for n in range(0, len(markElement)):
            #print delX[n], ' ', 'rft'            
            delX.pop(markElement[n]-n)                
    else:      
        zeros = [0 for x in range(length)]
        
        
print 'rgr'
for n in output:
    print n