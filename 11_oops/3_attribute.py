#class attribute -> belong to class
#instance attribute -> belong to indivisual

class student:
    collage_name="Abes engineering College,Ghaziabad" #class attribute
    estd=2000                                         #class attribute

    def __init__(self,name,cgpa):
        self.name=name                                 #instance attribute
        self.cgpa=cgpa                                 #instance attribute
        self.estd=1990                               #instance attribute ->common but high priority

s1=student("Alok",9.2)

print(s1.collage_name,s1.name,s1.cgpa,s1.estd)