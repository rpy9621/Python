import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
a=int(input("Enter the number to print it table :\n"))
while(a<=-11):
    a=a*a
    a=a-1
    print(a)