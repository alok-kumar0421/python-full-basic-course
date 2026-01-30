info=[
    ("alok","english"),
    ("alok","sanskrit"),
    ("adi","computer"),
    ("mona","english"),
    ("alok","english"),
    ("raja","math")
]
s=set() #declare set
for t in info:
    s.add(t[0])

print(s)

for t in info:
    if(t[1]=="english"):
        print(t[0])

# ------------make in dictionary-------
dict={}

for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)