#!/usr/bin/python3

from sys import argv
import operator

def calc_gc(dna_string):
#calculate the GC content
   
   #count the number of G's and C's
    gc_count = dna_string.count("G") + dna_string.count("C") 
    
    #count the total number of characters in the DNA string
    dna_length = len(dna_string)

    gc_content = gc_count/dna_length
    
    return gc_content

def iterate_ID(fasta):
#iterate and store FASTA IDs
    with open (fasta) as infile:
        lines = [line.strip() for line in infile]
        IDs = []
        gc_cont= []
        gc_index = -1
        ID_index = -1
        #iterate through lines and call the calc_gc function for each DNA string
        for i, fasta_line in enumerate(lines):
            if fasta_line.startswith(">"):
                IDs.append(fasta_line[1:])
                ID_index += 1
            else:
                gc_cont.append(calc_gc(fasta_line))
        
        #find maximum value from the gc content list
        max_gc = max(gc_cont)
        max_index = gc_cont.index(max_gc)

        print (str(IDs[max_index]) + "\n" + str(max_gc))
        
        

if __name__ == "__main__":
       
    infile = argv[1]
    iterate_ID(infile)
     
