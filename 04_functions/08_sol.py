# def print_kwargs(name, power):
#     print("name: ", name, " power: ", power)
    
# print_kwargs(name="Arti", power="super power")    


def print_kwargs(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")
        
print_kwargs(name= "Arti", power= "super-power")        
print_kwargs(name= "Arti")       
print_kwargs(name= "Arti", power= "lower-power", enemy= "ENEMY")       