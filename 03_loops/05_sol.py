s = input("enter your string")

for i in s:
    print(i)
    if(s.count(i) ==1 ):
        print("first non repeated char is :", i)
        break