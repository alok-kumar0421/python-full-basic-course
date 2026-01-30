class Employee:
    start_time="10am"
    end_time="6pm"

    def changeSrtTime(self,newtime):
        self.start_time=newtime
    
class Teacher(Employee):  #inherit employee properties
    def __init__(self,subject):
        self.subject=subject


t1=Teacher("COA")
t1.changeSrtTime("11am")
print(t1.subject,t1.start_time,t1.end_time)