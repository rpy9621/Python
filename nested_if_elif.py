
a = int(input("Enter the num to check it:"))
if (a<0):
 print("Less than zero")
elif (a>0):
 if(a>1 and a<=10):
  print("a is btween 1 to 10")
 elif(a>11 and a<=20):
  print("a is between 11 to 20")
 else:
   print("a is greater than 20")
else:
 print("a is eaual to zero")
