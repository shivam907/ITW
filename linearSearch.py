l=list(map(int,input().split()))
n=int(input("Enter no to be searched: "))
d=5
for i in l:
    if(n==i): 
        print("Element found ") 
        break
    else:
         d+=1

if d==len(l):
    print("Element not found")