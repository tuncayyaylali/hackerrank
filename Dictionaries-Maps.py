# Dictionaries&Maps
n = int(input())
phone_list=dict()
for _ in range(n):
    a= input()
    if len(a)>1:
        a= a.split(" ")
        phone_list[a[0]] = a[1]
while True:
    try:
        a=input()
        if a in phone_list:
            print(f"{a}={phone_list.get(a)}")
        else:
            print("Not found")
    except:
        break
