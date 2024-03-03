n=int(input("enter a number:\n"))
num=0
r=0
while (n!=0):
    num=n%10
    r+=num+1
    n=n//10
print("sum:",r)
