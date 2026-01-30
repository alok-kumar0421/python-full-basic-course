class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        self.name=name
        super().__init__(salary)
        Student.__init__(self,gpa)

t1=TA("2500000000",9.3,"shtadha")

print(t1.gpa)