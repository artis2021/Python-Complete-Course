username = "Arti"

def func():
    # username = "chai"
    print(username)
    
print(username)
func()   



# def func1(y):
#     z = x+ y
#     return z
# x = 99
# print(func1(2))

x = 99
# def func2():
#     global x
#     x= 88
  
# func2()    
# print(x)   


# def func3():
#     x= 88
#     def f1():
#         print(x)
#         return f1
#     ans = f1()
#     ans()
#     return ans

    
# func3()    

def chaicode(num):
    def actual(x):
        return x ** num
    return actual

f = chaicode(2)
g = chaicode(3)

print(f(3))
print(g(3))
     
     
     

