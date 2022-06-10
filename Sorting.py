import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps=0
    for i in range(n):
        gecici=0
        for j in range(n-1):
            gecici=0
            if a[j] > a[j+1]:
                gecici = a[j]
                a[j] = a[j+1]
                a[j+1] = gecici
                numberOfSwaps+=1
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
