x=int(input("enter number :"))
c=1
for i in range(1,x+1):
    c=c*i
print(c)

# ---------2nd method---------------
# k=1
def fact(n):
    k=1
    for l in range(1,n+1):
        k=k*l
    return k
print(fact(6))