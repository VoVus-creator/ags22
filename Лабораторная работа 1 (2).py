# -- coding: utf-8 --
import random as rand

a = int(input("n= "))

if a>0:
    her=[-3+6*rand.random() for i in range(a)]
    print(her)
    sr=sum(her)/len(her)
    for k,x in enumerate(her):
        if x==0:
            her[k]=sr
    print(her)