#!/usr/bin/python3

from sys import argv

def read_fasta(filename):
    IDlist = []
    seqlist = []
    currentseq = ""

    with open (filename) as f:
        for line in f:
            line = line.strip()   
            
            # read ID and add it to the ID list, then read and store the corresponding sequence
            if line.startswith(">"):
                id = line[1:].strip()
                IDlist.append(id)
                
                if currentseq != "":
                    seqlist.append(currentseq)
                currentseq = ""
            else:
                #extract all lines of sequence data and add it to single string
                currentseq += line.strip()

        #need this so the last sequence will be added
        seqlist.append(currentseq)

    return seqlist

def find_consensus(fasta):

    A = []
    C = []
    G = []
    T = []   

    for i in read_fasta(fasta):
        print(i)
        for j in i:
            A_count = j.count("A")

            
            print(j)
            A_count[k] = "!"
            print(A_count)

''' 
            C_count[j] += i[j].count("C")
            G_count[j] += i[j].count("G")
            T_count[j] += i[j].count("T")

    return A_count, C_count, G_count, T_count
'''
    
if __name__ == "__main__":
    file = argv[1]
    
    print(*find_consensus(file),sep="\n")
    

            
