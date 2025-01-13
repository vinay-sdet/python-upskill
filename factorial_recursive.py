def fact(num):
    if (num ==0 or num==1):
        return 1
    return num *fact(num-1)


inputnum = (int(input("Enter number for factorial: ")))
print(f"Factorial of {inputnum} is ", fact(inputnum))
