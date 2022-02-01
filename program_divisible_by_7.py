num1=2000
num2=3200
for i in range(num1,num2+1):
    if i%7==0:
        if i%5 ==0:
            continue
        else:
            print(i,end=",")   
           