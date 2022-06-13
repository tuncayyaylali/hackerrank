if __name__ == '__main__':
    N = int(input())
    Liste=[]
    for i in range(N):
        komut=input().split()
        if komut[0]=="insert":
            Liste.insert(int(komut[1]), int(komut[2]))
        elif komut[0]=="remove":
            Liste.remove(int(komut[1]))
        elif komut[0]=="append":
            Liste.append(int(komut[1]))
        elif komut[0]=="sort":
            Liste.sort()
        elif komut[0]=="pop":
            Liste.pop()
        elif komut[0]=="reverse":
            Liste.reverse()
        else:
            print(Liste)
