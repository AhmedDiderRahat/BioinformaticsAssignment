# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 01:40:06 2017

@author: AD-Rahat
"""

import codecs

f_in = codecs.open("input.txt","r", encoding="UTF-8")
s = []
e = []
v = []
putative = 0
for w in f_in:
    w = w.strip()
    list = w.split()
    s.append(int(list[0]))
    e.append(int(list[1]))
    v.append(int(list[2]))    
    putative = putative+1 
f_in.close()

mx = max(e)
mn = min(s)

print putative

for i in range(0, len(s)):
    for j in range(i, len(s)):
        if s[i] > s[j]:
            s[i], s[j] = s[j], s[i] 
            e[i], e[j] = e[j], e[i]
            v[i], v[j] = v[j], v[i]

for i in range(0, len(s)):
    print s[i], e[i], v[i]

output = [0 for i in range(mx-(mn-2))]
print output[1:]

for i in range(0, putative):
    start = s[i]
    end = e[i]
    score = v[i]
   
    output[end] = output[start]+score
    print start, end, score
    for j in range(end+1, len(output)):
        if output[j] >= output[end]:
            break
        output[j] = output[end]
    print output[1:]
print '\nOutput: ',
print output[1:]