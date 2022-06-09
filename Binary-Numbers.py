# Binary Numbers
import math
import os
import random
import re
import sys

def bolen(bolunen):    
    bolum = int(bolunen/2)
    kalan = bolunen - 2*bolum
    return bolum, kalan

if __name__ == '__main__':
    n = int(input().strip())
    liste=[]
    if n<=0:
        liste.append(0)
    if n == 1:
        liste.append(1)
    while n>1:
        n, kalan = bolen(n)
        if n == 1:
            liste.append(kalan)
            liste.append(n)
            break
        liste.append(kalan)
        
    sonuc = "".join([str(x) for x in liste[::-1]])
    sonuc = sonuc.split("0")
    sonuc = [len(x) for x in sonuc]
    print(max(sonuc))
