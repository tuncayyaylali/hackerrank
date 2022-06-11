import numpy as np
N=int(input())
liste=[]
for _ in range(N):
    liste.append(list(map(float, input().split())))
sonuc = np.array(liste)
det = np.linalg.det(sonuc)
print(round(det, 2))
