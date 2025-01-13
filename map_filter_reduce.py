from functools import reduce

#Example of map

num_list = [1,2,3,4,5,6,7,8]

square = lambda x: x*x

sq_list = map(square,num_list)

print(list(sq_list))

#Example of filter

def even(num):
    if (num%2 == 0):
        return True
    return False

onlyEven=filter(even,num_list)
print(list(onlyEven))

#Example of reduce

def sum(a,b):
    return a+b

mul = lambda x,y: x*y

print(reduce(sum,num_list))
print(reduce(mul,num_list))
    