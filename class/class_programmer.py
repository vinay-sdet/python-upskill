class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language


p1 = Programmer("Vinay","5000000","Python")
p2 = Programmer("Vijay","5000000","JavaScript")

print(p1.name, p1.salary, p1.language)
print(p2.name, p2.salary,p2.language)