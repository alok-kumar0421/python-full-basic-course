# range - > range(6)=[0,6-1]=[0,5]

for i in range(5):
    print(i)
#--------count vowel----------
v=0
word="artificial intelligent"
for ch in word:
    if(ch=="a" or ch=='e' or ch=='i' or ch=='o'or ch=='u'):
        v+=1
print(v)

for j in range(1,10,4): #range(str,end,step)
    print(j)