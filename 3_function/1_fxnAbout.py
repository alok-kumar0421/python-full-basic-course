#def->defination

def hallo():
    print("hello")

hallo()
# ----------return fxn----------
def sum(a,b):
    print(a+b)

sum("a","b")

# ---------avg function--------
def avg(a,b,c):
    print((a+b+c)/3)
avg(5,6,3)

# --------default func----------
def avg(a,b=2):
    print((a+b)/2)
avg(2,3)