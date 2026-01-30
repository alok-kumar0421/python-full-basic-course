t=(1,2,3,2,2,2,2,4,5)
sum=0
for i in t:
    sum=sum+i

print(f"sum of all are:{sum}")

# ---------first occuring-------
print(t.index(2))

# -------------count alll occurance-------
print(t.count(2))