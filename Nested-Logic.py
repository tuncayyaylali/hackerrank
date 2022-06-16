import datetime
dr, mr, yr = map(int, input().split())
returned_date = datetime.datetime(yr, mr, dr)
dd, md, yd = map(int, input().split())
due_date = datetime.datetime(yd, md, dd)
difference = returned_date-due_date
if difference.days<=0:
    print(0)
else:
    if yr==yd and mr==md:
        print(15*difference.days)
    elif yr==yd and mr!=md:
        print(500*(mr-md))
    else:
        print(10000)
