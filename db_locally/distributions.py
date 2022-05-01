import datetime

def player_distribution (lvl:int, arr:list):
   
    if lvl <=10: arr[0]+=1
    if 10< lvl <=20: arr[1]+=1
    if 20< lvl <=30: arr[2]+=1
    if 30< lvl <=40: arr[3]+=1
    if 40< lvl <=50: arr[4]+=1
    if 50< lvl <=60: arr[5]+=1
    if 60< lvl <=70: arr[6]+=1
    if 70< lvl <=80: arr[7]+=1
    if 80< lvl <=90: arr[8]+=1
    if 90< lvl: arr[9]+=1
    
    return arr


#t0 = datetime.datetime.now()-datetime.datetime.now()

t1 = datetime.datetime.now()
t0 = t1 - datetime.timedelta(days=1)
def battlelogs_distribution(t:datetime,arr:list):
    if t0 < t < t1:
        if t.hour == 0 or t.hour == 1:arr[0]+=1
        if t.hour == 2 or t.hour == 3:arr[1]+=1
        if t.hour == 4 or t.hour == 5:arr[2]+=1
        if t.hour == 6 or t.hour == 7:arr[3]+=1
        if t.hour == 8 or t.hour == 9:arr[4]+=1
        if t.hour == 10 or t.hour== 11:arr[5]+=1
        if t.hour == 12 or t.hour== 13:arr[6]+=1
        if t.hour == 14 or t.hour== 15:arr[7]+=1
        if t.hour == 16 or t.hour== 17:arr[8]+=1
        if t.hour == 18 or t.hour== 19:arr[9]+=1
        if t.hour == 20 or t.hour== 21:arr[10]+=1
        if t.hour == 22 or t.hour== 23:arr[11]+=1

    return arr



def level_distribution_result_schema (n:int, arr :list):
    x= [10,20,30,40,50,60,70,80,90,100]
    for i in range(n):
        arr[i]= {
            x[i]: arr[i]
        }
    return arr


def battles_distribution_result_schema(n:int, arr: list):
    x = ["00:00","02:00","04:00",
        "06:00","08:00","10:00",
         "12:00","14:00","16:00",
         "18:00","20:00","22:00"]
    for i in range(n):
        arr[i]= {
            x[i]: arr[i]
        }
    return arr