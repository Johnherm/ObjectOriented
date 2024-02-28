# #First Method
# #The following using of class is the most difficult and it can be happen code error
# class Employee:   #24 code lines
#     pass
# emp_1 = Employee()
# emp_2 = Employee()
# #This is first employee data
# emp_1.first = "Corey"
# emp_1.last = "Schafer"
# emp_1.email = "Corey.Schafer@gmail.com"
# emp_1.pay = 50000
# #This is second employee data
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.user@gmail.com"
# emp_2.pay = 60000
# #Printing out employees information
# print("")
# print(f"first name of first employee is  {emp_1.first}")
# print(f"last name of {emp_1.first} is {emp_1.last}")
# print(f"email of {emp_1.first} is {emp_1.email}")
# print(f"Salary of {emp_1.first} is {emp_1.pay}")
# print("")
# print(f"first name of second employee {emp_2.first}")
# print(f"last name of {emp_2.first} is {emp_2.last}")
# print(f"email of {emp_2.first} is {emp_2.email}")
# print(f"Salary of {emp_2.first} is {emp_2.pay}")

#Second Method
#The following method is best one. only 17 code lines
class Employee():
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com" # or just write email
        self.pay = pay
emp_1 = Employee("Corey","Schafer","Corey.Schafer@gmail.com",50000) #This is first employee data
emp_2 = Employee("Test","User","Test.user@gmail.com",60000) #This is second employee data
# #Printing out employees information
print(f"first name of first employee is  {emp_1.first}")
print(f"last name of {emp_1.first} is {emp_1.last}")
print(f"email of {emp_1.first} is {emp_1.email}")
print(f"Salary of {emp_1.first} is {emp_1.pay}")
print("")
print(f"first name of second employee {emp_2.first}")
print(f"last name of {emp_2.first} is {emp_2.last}")
print(f"email of {emp_2.first} is {emp_2.email}")
print(f"Salary of {emp_2.first} is {emp_2.pay}")
