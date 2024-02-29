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

#This is the difference between function and class 
def firstEmployee():
    first = "Corey"
    last = "Schafer"
    email = "coery.schafer@gmail.com"
    pay =  50000
    print(first, last, email, pay)
def secondEmployee():
    first = "Test"
    last = "User"
    email = "test.user@gmail.com"
    pay = 60000
    # print(first, last, email, pay)
    print(first, last, email, pay)
firstEmployee()
secondEmployee()