# RomanNumeralReduction
def RomanNumeralReduction(strParam):

  dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  strParam = list(strParam)
  toplam=0
  for i in strParam:
    toplam += dict[i]
  roman=[]
  while toplam/1000 >=1:
    toplam-=1000
    roman.append("M")
  while toplam/500 >=1:
    toplam-=500
    roman.append("D")
  while toplam/100 >=1:
    toplam-=100
    roman.append("C")
  while toplam/50 >=1:
    toplam-=50
    roman.append("L")
  while toplam/10 >=1:
    toplam-=10
    roman.append("X")
  while toplam/5 >=1:
    toplam-=5
    roman.append("V")
  for i in range(toplam):
    roman.append("I")  
  return "".join(roman)
