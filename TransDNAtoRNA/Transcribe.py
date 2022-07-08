#!/usr/bin/python3

f = input("enter filename: ")

with open (f,"r") as dna:
    for line in dna:
        print (line.replace("T","U"))




