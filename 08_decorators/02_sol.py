def debug(func):
    def wrapper(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k}= {v} " for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_val} and kwargs {kwargs_val}")
        return func(*args, **kwargs)
    
    return wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name, greeting= "Hello"):
    print(f"{greeting}, {name}")
    
hello()    
greet("Arti", greeting= "Good morning")    