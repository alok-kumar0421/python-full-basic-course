class Employee:
    def designation(self):
        print("designation=employee")

class Teacher(Employee):
    def designation(self):
        print("designation=Teacher")  #overriding

t1 = Teacher()

t1.designation()