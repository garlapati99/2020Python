class Employee:
    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.email = first + "." + second + "@company.com"




emp1 = Employee("Kalyan", "Garlapati", 30000)
emp2 = Employee("Test", "Test", 60000)

print(emp1.first)
print(emp1.email)