#!/usr/bin/python3

from sys import argv

filename = argv[1]

transDict = {'A':'T','T':'A','G':'C','C':'G'}

with open (filename) as dna:
    for line in dna:
        print ("".join(transDict[base] for base in line.strip()[::-1]))

        
    
