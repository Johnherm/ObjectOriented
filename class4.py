class Employee():
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com" # or just write email
        self.pay = pay
    def fullname1(self):
        return f"{self.first, self.last, self.email, self.pay}"
    def fullname2(self):
        return f"{self.first, self.last, self.email, self.pay}"
emp_1 = Employee("Corey","Schafer","Corey.Schafer@gmail.com",50000) #This is first employee data
emp_2 = Employee("Test","User","Test.user@gmail.com",60000) #This is second employee data
print(emp_1.fullname1())
print(emp_2.fullname2())
