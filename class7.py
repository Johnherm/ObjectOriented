class Employee():
    num_of_employees = 0
    raise_amt = 1.04
    def __init__(just, first, last,pay):
        just.fname = first
        just.lname = last
        just.email = first + "."+ last + "@gmail.com"
        just.annual = pay
        Employee.num_of_employees = Employee.num_of_employees + 1
    def full_name(just):
        return f"{just.fname, just.lname}" 
    def apply_raise(just):
        just.pay = int(just.pay* just.raise_amt)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

# Creating a variable or assign the employees

emp_1 = Employee("Corey", "Jackson",50000)
emp_2 = Employee("Test", "Employee",60000)
#Print out the employee data or information
emp_1.set_raise_amt(1.06) 
Employee.set_raise_amt(1.05)
print(emp_1.full_name())
print(emp_2.full_name())
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
