#!/usr/bin/python3

Acount = 0
Ccount = 0
Gcount = 0
Tcount = 0

with open('rosalind_dna-2.txt',"r") as file:
	for line in file:
		Acount = line.count("A")
		Ccount = line.count("C")
		Gcount = line.count("G")
		Tcount = line.count("T")	

print(str(Acount) + " " + str(Ccount) + " " + str(Gcount) + " " + str(Tcount))	 
