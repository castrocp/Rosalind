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

    return find_overlap(IDlist, seqlist)

def find_overlap(ids,seqs):
    
    #adjecency list to store overlapping sequences
    adj_list = []
    
    # s and t to keep track of which index of the "to" and "from" in the directed graph
    s = 0
    #iterate each fasta sequence
    for seq in seqs:
        t = 0
        #compare sequence to all sequences that aren't the same, or itself 
        for i in seqs:
            if seq == i:
                t += 1
                
            if seq != i:
                if seq[-3:] == i[:3]:  
                    adj_list.append((ids[s] + " " + ids[t]))
                t += 1
        s += 1   
    
    return adj_list

if __name__ == "__main__":
    file = argv[1]
    
    print(*read_fasta(file),sep="\n")
    

            
