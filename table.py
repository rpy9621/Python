import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
a=int(input("Enter the number where you want to find table :\n"))
for n in range(1,11):
    print(a,"*",n,"=",n*a)