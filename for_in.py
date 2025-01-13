num = int(input("Enter a number: "))

# for i in range(1,11):
#     print(i*num)

table = [i*num for i in range(1,11)]
print(table)