# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import math
n = int(input("Enter 1 if you want to find power\nEnter 2 if you want to find square root\nEnter (1/2): "))
if(n==1):
    num = int(input("Enter number "))
    pow = int(input("Enter power "))
    print("\n Power is {}".format(num**pow))
elif(n==2):
    num = int(input("Enter number "))
    print("Square root is {}".format(math.sqrt(num)))
