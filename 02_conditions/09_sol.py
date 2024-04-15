year1 = input("enter your year")
year = int(year1)
flag = True
if(year % 400 ==0 ):
    flag = True
elif(year % 100 ==0 ):
    flag = False
elif(year % 4 ==0 ):
    flag = True
else:
    flag = False
    
ans = "leap year" if flag == True else "not leap year"  
print("your year is: ", ans)                