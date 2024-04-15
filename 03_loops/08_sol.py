n = int(input("enter your number"))

for i in range(2, n):
    if(n % i == 0):
        print("Your number is not prime")
        exit()
print("your number is prime")        