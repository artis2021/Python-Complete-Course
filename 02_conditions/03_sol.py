score = int(input("your score "))
grade = "A"

if score >= 101:
    print("again enter your score")
    exit()
    

if score >= 85:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(grade)                