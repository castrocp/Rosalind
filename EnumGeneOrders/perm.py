#!/usr/bin/python3

def factorial(n):
    n = int(n) 
    i = 1
    while n  >= 1:
        i = i * n
        n = n - 1
    
    return i

def perm(lst):
    if len(lst) == 0:
        return []
	
    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        remlst = lst[:i] + lst[i+1:]

        for p in perm(remlst):
            l.append([m] + p)

    return l
    
if __name__ == "__main__":
    data = list("12345")
    n = 5
    
    print (factorial(n))
    
    for p in perm(data):
        print (*p)

