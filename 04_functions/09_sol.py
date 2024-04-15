def even_num(limit):
    # li = []
    for i in range(2, limit+1, 2):
        yield i
        # li.append(i)
    # return li    
        
for num in even_num(10):
    print(num)    