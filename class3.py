class Employee():
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com" # or just write email
        self.pay = pay
emp_1 = Employee("Corey","Schafer","Corey.Schafer@gmail.com",50000) #This is first employee data
emp_2 = Employee("Test","User","Test.user@gmail.com",60000) #This is second employee data
# #Printing out employees information
print("Printing out each information of employee")
print("") # This is just for space
print(f"first name of first employee is :  {emp_1.first}")
print(f"last name of {emp_1.first} is : {emp_1.last}")
print(f"email of {emp_1.first} is : {emp_1.email}")
print(f"Salary of {emp_1.first} is : {emp_1.pay}")
print("") # This is just for space
print(f"first name of second employee : {emp_2.first}")
print(f"last name of {emp_2.first} is : {emp_2.last}")
print(f"email of {emp_2.first} is : {emp_2.email}")
print(f"Salary of {emp_2.first} is : {emp_2.pay}")
# Printing out all information at once 
print("Printing out all information of employee at once ")
print(f"{emp_1.first, emp_1.last, emp_1.email, emp_1.pay}")
print(f"{emp_2.first, emp_2.last, emp_2.email, emp_2.pay}")
