#d-day 카운트

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

import datetime
over = 0
d_day = int(str(datetime.date(y2,m2,d2) - datetime.date(y1,m1,d1)).split()[0])
for i in range(0,1000) :
    if(((i%4 == 0 and i % 100 != 0)) or i % 400 ==0):
        over+= 366
    else : 
        over+= 365
if(d_day >= over):
    print('gg')
else :
    print('D-'+str(d_day))

    
