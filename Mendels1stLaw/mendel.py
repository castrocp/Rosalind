#!/usr/bin/python3
# input file will be in the form (k,m,n) representing the number of organisms in population
# script will calculate probability that offspring will possess at least 1 dominant allele
# given that the parents are chosen at random from population

from sys import argv

def dominant_prob(infile):
    with open (infile) as organisms:
        for line in organisms:
            line = line.split()

            #hom = # of homozygous dominant organisms. het = heterozygous. rec = homozygous recessive
            hom = int(line[0])
            het = int(line[1])
            rec = int(line[2])
            
            #total population
            pop = hom + het + rec

            prob = ( 2*(hom*het + hom*rec) + hom*(hom-1) + het*(.75*het - .75 + rec) ) / (pop * (pop -1) )  
            
            return ("%.5f" % prob)

if __name__ == "__main__":
    infile = argv[1]
    print (dominant_prob(infile))
