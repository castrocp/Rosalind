#!/usr/bin/python3

from sys import argv


map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
                "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
                    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
                        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                                        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                                            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                                "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                                    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                                                        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                                                            "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                                                "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                                                    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

#to determine how many codons can make a given amino acid
def frequency_of_aminoacid():
    freq = {}
    for k,v in map.items():
        if not v in freq:
            freq[v] = 0
        freq[v] += 1
    return freq

#determine how many combinations of codons can make up the entire amino acid sequence
def count_RNA_strings(aminoacids):
    f = frequency_of_aminoacid()
    n = f["Stop"]
    
    #multiply the number of ways to code each for amino acid by the number of ways to code for a stop codon (3)
    for c in aminoacids:
        n *= f[c]

    return n 

if __name__ == '__main__':
    infile = argv[1]

    with open (infile) as sequence:
        for line in sequence:
            line = line.strip()
            print (count_RNA_strings(line) % 1000000)

