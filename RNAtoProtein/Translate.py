#!/usr/bin/python3

from sys import argv
def main():
    infile = argv[1]

    def translate_rna(file):
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
       
        with open (file) as rna:
            for line in rna:
                line = line.strip()
                codons = [line[i:i+3] for i in range(0,len(line), 3)]
               
               #brackets were put around the the section being joined, so that it could be a joined list and printed on one line
                print("".join([map[codon] for codon in codons]))
                

    translate_rna(infile)

if __name__== '__main__':
    main()
                        
