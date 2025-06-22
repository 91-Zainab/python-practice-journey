#Create a class "programmer" for storing information of few programmers working at microsoft.

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin 
z = programmer ("Zainab", 10000000, 45402)
print(z.name, z.salary, z.pin)
J = programmer ("Joy", 1000000,45420)
print(J.name, J.salary, J.pin)

        