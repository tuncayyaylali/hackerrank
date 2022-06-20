import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    list=[]
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if "@gmail." in emailID:
            list.append(firstName)
list.sort()
for i in list:
    print(i)       
