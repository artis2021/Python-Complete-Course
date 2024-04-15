import math
def circle(r):
    a = round(math.pi * r * r, 2)
    p = round(math.pi * 2* r, 2)
    return a, p

print(circle(7))