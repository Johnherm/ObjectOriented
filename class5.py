#Now let us do a class for ASTU fresh students
class FreshStudents():
    def __init__(self,first, last, id,department, bach, section):
        self.first = first
        self.last = last
        self.id = id
        self.department = department
        self.bach = bach
        self.section = section
    def firstStudent(self):
        return f"{self.first, self.last, self.id, self.department, self.bach, self.section}"
    def secondStudent(self):
        return f"{self.first, self.last, self.id, self.department, self.bach, self.section}"
s1 = FreshStudents("Addisu","Gebru","ugr/22863/13","Mechanical",4,1)
s2 = FreshStudents("Sefu","Tamirat","ugr/23245/13","Architecture",4,2)
print(s1.firstStudent())
print(s2.secondStudent())





