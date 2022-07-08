#!/usr/bin/python3
from sys import argv

def hamming(pair):
    with open (pair) as infile:
        seq1, seq2 = infile.readlines()
        seq1 = seq1.strip()
        seq2 = seq2.strip()
    
    #calculate hamming distance by keeping track of symbols that don't match between the two sequences
    length = len(seq1)
    dist = 0

    for i in range(0,length):
        if seq1[i] != seq2[i]:
            dist += 1

    return dist


if __name__ == "__main__":
    rosalind_file = argv[1]
    print (hamming(rosalind_file))
