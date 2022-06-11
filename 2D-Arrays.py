import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    liste = []
    for satir in range(4):
        for sutun in range(4):
            goz_toplam=0
            for satir_artis in range(3):
                for sutun_artis in range(3):
                    if satir_artis==1 and sutun_artis==0:
                        continue
                    elif satir_artis==1 and sutun_artis==2:
                        continue
                    goz_toplam += arr[satir+satir_artis][sutun+sutun_artis]
            liste.append(goz_toplam)
    print(max(liste))
