import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
fact =1
n=int(input("Enter the number where you want to find factorial :\n"))
for i in range(1,n+1):
    fact=fact*i
print("Factorial is number is :",fact)        