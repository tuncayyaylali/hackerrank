# SimpleMode
def SimpleMode(arr):
    dict={}
    if len(arr)==0:
        return -1
    for i in arr:
        count=0
        for j in range(len(arr)):
            if arr[j] == i:
                count+=1
        dict[i]=count
    max_values = max(set(dict.values()))
    if max_values==1:
        return -1
    else:
        for number, sayim in dict.items():
            if sayim == max_values:
                return number
