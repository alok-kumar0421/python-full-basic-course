#create a list of square of 0 to 10
sq=[i*i for i in range(11)]
print(sq)

#odd number till 10
even = [i for i in range(11) if(i%2==0)]
print(even)

#make all list megative number to zero
x=[2,4,-5,7,-6,3,-6,3,-7]
pos=[0 if i<0 else i for i in x]
print(pos)