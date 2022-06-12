n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    komut = input().split()
    if komut[0] == "pop":
        s.pop()
    elif komut[0] == "discard":
        s.discard(int(komut[1]))
    else:
        s.remove(int(komut[1]))
print(sum(s))
