# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:26:57 2017

@author: AD-Rahat
"""    


demoSequence = []    

def createRandMotive():
    cnt = 0
    temp = ['A', 'T', 'G', 'C']    
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                for a in range(0, 4):
                    output = temp[i] + '' + temp[j] + '' + temp[k] + '' + temp[a]
                    demoSequence.insert(cnt, output)
                    #print cnt, '-> ', output
                    cnt = cnt+1                    


def mutation(s1, s2, m):
    cnt = 0
    for index in range (0, len(s1)):
        if s1[index] != s2[index]:
            cnt = cnt+1
            if cnt > m:
                return False
    return True
            
            


def motifFindingAlgo(sequences, l, m, seqNum):
    consensous = []
    ccnt = 0
    for candidate in demoSequence:
        raw = []
        rcnt = 0
        raw.insert(rcnt, candidate)
        rcnt = rcnt+1
        for sequence in sequences:
            for i in range (0, len(sequence)-(l-1)):
                temp = sequence[i:i+l]           
                if mutation(temp, candidate, m):
                    raw.insert(rcnt, temp)
                    rcnt = rcnt+1
                    break
                
        
        if len(raw) == seqNum+1:
            consensous.insert(ccnt, raw)
            ccnt = ccnt+1
            
    return consensous

sequences = ['ATGATGTCT', 'GAACGTCTT', 'GTGTCTGTC', 'ATGCCATAT']
createRandMotive()

print '\n\n'

consious = motifFindingAlgo(sequences, 4, 1, 4)
for raw in consious:
    for element in raw:
        print element
    print '\n'

cnt = 0



temp = ['A', 'T', 'G', 'C']     
for raw in consious:  
    outRaw = []
    outr=0
    for i in range (0, len(raw[0])):
        dictionary = {}
        for k in range(0,4):
            dictionary[temp[k]] = 0
        for j in range(0, len(raw)):      
            if raw[j][i] in dictionary:
                value = dictionary[raw[j][i]] + 1
                dictionary[raw[j][i]] = value
            else:
                dictionary[raw[j][i]] = 1
        outRaw.insert(outr, dictionary)
        outr = outr+1
        print dictionary
    print 