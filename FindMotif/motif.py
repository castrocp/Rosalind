#!/usr/bin/python3

#given two dna strings, seq and ref, find all locations of seqas a substring of ref

#loop through reference, and see if ref[start:length of seq] == seq
from sys import argv

def match_motif(ref, seq):
    positions = []
    for i in range(0,len(ref)-len(seq)+1):
        print (ref[i:i+len(seq)], seq)
        if ref[i:i+len(seq)] == seq:
            positions.append(i+1)
                
    print(*positions,sep=" ")


if __name__ == "__main__":
    infile = argv[1]

    with open (infile) as seqs:
        seq1, seq2 = seqs.readlines()
        seq1 , seq2 = seq1.strip(),seq2.strip()
    
    match_motif(seq1,seq2)
