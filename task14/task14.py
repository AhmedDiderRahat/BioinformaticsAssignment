# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:56:39 2017

@author: AD-Rahat
"""

def LCS(s1, s2):
    print s1, ' ', s2
    
    flag=[]

    matrix = []
    len1 = len(s1)
    len2 = len(s2)
    for i in range(0, len1+1):
        raw = []       
        fraw = []
        for j in range(0, len2+1):
            raw.append(0)
            fraw.append('N')
        matrix.append(raw)
        flag.append(fraw)
    
    for i in range (1, len1+1):
        for j in range (1, len2+1):
            if s1[i-1] == s2[j-1]:
                flag[i][j] = 'D'
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                if matrix[i-1][j] >= matrix[i][j-1]:
                    flag[i][j] = 'U'
                else:
                    flag[i][j] = 'L'
                
    for i in range (0, len1+1):
        for j in range (0, len2+1):
            print matrix[i][j],
        print
    print '\n\n'
    
    for i in range (0, len1+1):
        for j in range (0, len2+1):
            print flag[i][j],
        print
        
    i = len1
    j = len2
    output = []
    while(True):
        if flag[i][j]=='N':
            break
        elif flag[i][j] == 'D':
            output.append(s1[i-1])
            i = i-1
            j = j-1
        elif flag[i][j] == 'L':
            j = j-1
        elif flag[i][j] == 'U':
            i = i-1
            
    output.reverse()
    print 
    temp=''
    for ch in output:
        temp = temp + ch
    print temp


LCS('RAHIB', 'RAHAB') 