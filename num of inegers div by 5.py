n=int(input("enter a number:\n"))
sum=0
for i in range(1,n+1):
    if(i%5==0):
        print(i)
        sum+=i
print("sum:",sum)
