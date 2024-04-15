dist = int(input("enter distance"))

if(dist < 3):
    print("walk")
elif(dist >=3 and dist <= 15):
    print("bike")
elif(dist > 15):
    print("car")        