prime = j = 1
c=0
l=[1]
n=int(input("Enter no: "))

for i in range(1,n):
    for j in range(1,i):
        if(i%j==0):
            c+=1
    if(c==1):
        l.append(i)
    c=0

print(l)