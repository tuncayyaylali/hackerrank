import numpy
katsayilar = input().split()
x = float(input())
sonuc=0
for i in range(len(katsayilar)):
    sonuc+=float(katsayilar[-1-i])*(pow(x, i))
print(sonuc)
