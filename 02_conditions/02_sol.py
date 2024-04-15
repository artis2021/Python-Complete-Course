age = int(input("your age"))
day = input("enter day")

price = 12 if age >= 18 else 8
price = price-2 if day == "wednesday" else price
print(price)