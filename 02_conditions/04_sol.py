fruit = input("enter fruit")
color = input("color of fruit")   

if(fruit != "banana"):
    print("enter banana only")
    exit()
    
if(color == "green"):
    print("banana is unripe")
elif(color == "yellow"):
    print("banana is ripe")
elif(color == "brown"):
    print("banana is rotten")
else:
    print("invalid colour")                 