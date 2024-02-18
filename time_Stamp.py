import time
t=time.strftime('%H:%M:%S')
print(t)
#taking time from system
hour=int(time.strftime('%H'))
#time taking input from the user
# hour=int(input("Enter the time : "))
print(hour)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
# if()
if(hour>=0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternnon")
else:
    print("Good Night") 
