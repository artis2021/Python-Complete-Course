password = input("enter your password")

strenth = ""
if(len(password) < 6):
    strenth = "weak"
elif(len(password) <= 10):
    strenth = "medium"
else:
    strenth = "strong"
    
print("your password is: ", strenth)           