print("********")
for i in range(10):
    print(i)

print("********")
for i in range(1,10):
    print(i)

print("********")
for i in range(1,10,2):
    print(i)

n = int(input("Enter a number: "))
print(f"Printing table for {n}")
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

print("********")

n = int(input("Enter a number: "))
print(f"Printing table for {n}")
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")