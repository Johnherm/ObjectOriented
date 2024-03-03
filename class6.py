class Employee():
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com" # or just write email
        self.pay = pay
        Employee.num_of_emps +=1
    def fullname1(self):
        return f"{self.first, self.last, self.email, self.pay}"
    def fullname2(self):
        return f"{self.first, self.last, self.email, self.pay}"
    def apply_raise(self):
        return self.pay*1.04
    def apply_fall(self):
        return self.pay*.1
    def apply_raise2(self):
        return self.pay* Employee.raise_amount 
    def apply_raise3(self):
        return self.pay* self.raise_amount 
#Printing out the amount of employees
print(Employee.num_of_emps)
emp_1 = Employee("Corey","Schafer","Corey.Schafer@gmail.com",50000) #This is first employee data
emp_2 = Employee("Test","User","Test.user@gmail.com",60000) #This is second employee data
#Printing out the amount of employees
print(Employee.num_of_emps)
print(emp_1.fullname1())
print(emp_2.fullname2())

print(emp_1.apply_raise())
print(emp_2.apply_raise())

print(emp_1.apply_fall())
print(emp_2.apply_fall())

print(emp_1.apply_raise2())
print(emp_2.apply_raise2())

print(emp_1.apply_raise3())
print(emp_2.apply_raise3())
# Printing out amount of raise
print(Employee.raise_amount)
print(emp_1.raise_amount)
#Printing out all information of variables and class
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)
#changing the amount of raise and displays the changes using the instance variables
Employee.raise_amount = 1.05
print(emp_1.apply_raise())
print(emp_2.apply_raise())

print(emp_1.apply_fall())
print(emp_2.apply_fall())

print(emp_1.apply_raise2())
print(emp_2.apply_raise2())

print(emp_1.apply_raise3())
print(emp_2.apply_raise3())

print(Employee.raise_amount)
print(emp_1.raise_amount)

#changing the amount of raise and displays the changes using the class variables
emp_1.raise_amount = 1.06
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

