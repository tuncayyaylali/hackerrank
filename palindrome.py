# Palindrome
def Palindrome(strParam):

  # code goes here
  strParam = strParam.replace(" ","")
  strParam_Reverse = strParam[::-1]
  if strParam_Reverse == strParam:
    return True
  else:
    return False
