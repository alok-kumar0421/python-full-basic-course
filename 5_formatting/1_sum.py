a=9
b=8
sum=a+b
print("sum of {} & {} is:={}".format(a,b,sum))

# ----index based formatt----------
print("sum of {1} & {0} is =:{2}".format(a,b,sum))

# -----value based format--------
print("value are {a} & {b}".format(a=6,b=7))
print("value are {} & {}".format(6,7))
# --------f-string--------
print(f"sum of {a} & {b} is {a+b}")

