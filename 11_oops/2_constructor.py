class student:
    def __init__(self,name,subject,cgpa): #use only one constructor and one init function per class
        self.name=name
        self.subject=subject
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa

s1=student("alok","python",9.2)
s2=student("momo","python",9.3)

print(s1.name,s1.cgpa)
print(s2.name,s2.cgpa)

print(f" {s1.name} has cgpa :{s1.get_cgpa()}")
