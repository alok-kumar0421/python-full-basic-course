class Employee:
    start_time="10am"
    end_time="6pm"

class admin_staff(Employee):
    def __init__(self,role):
        self.role=role

class accountant(admin_staff):
    def __init__(self,salary,role):
        self.salary=salary
        admin_staff.__init__(self,role) #calling..... to parent

acn1=accountant("25000","ca")

print(acn1.role,acn1.salary,acn1.start_time)