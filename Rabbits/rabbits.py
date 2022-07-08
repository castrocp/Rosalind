#!/usr/bin/python3

#Calculate the total number of rabbit pairs that will be present after n months
# if every pair of reproduction=age rabbits produces a littler of k rabbit pairs
#The input file contains two numbers, n and k


from sys import argv

def rabbitpair(months, litter):
    
    if months == 0:
        return 0

    if months == 1:
        return 1

    else:
        return rabbitpair(months-1,litter) + litter*rabbitpair(months-2,litter)
     
if __name__ == "__main__":
    #infile = argv[1]
    
    #with open (infile) as f:
     #   for line in f:
      #      months = int(line.strip()[0])
      #      litter = int(line.strip()[2]) #index "1" is the space in between 
    months = 29
    litter = 5
    print (rabbitpair(months,litter))



