# a,b = 0,1

# while(a<10):
#     print(a)
#     a, b=b, a+b

def fibonacci(num):
    a, b = 0,1

    while a<n:
        print(a, end=' ')
        a,b = b, a+b
        # temp = b
        # b = a + b
        # a = temp
    print()

n=int(input("Enter number: "))
fibonacci(n)
