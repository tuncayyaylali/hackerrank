import math
N = int(input())
for _ in range(N):    
    num=int(input())
    flag=False
    if num==1:
        print("Not prime")
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if (num%i)==0:
                flag=True
                break
        if flag:
            print("Not prime")
        else:
            print("Prime")   
