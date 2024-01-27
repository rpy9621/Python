#Strings in python
a=str(input("Enter the string : "))
print("Entered string is :",a)
print("Length of string is:",len(a))
b="He said, \"I want to eat an apple\"" #using escape sequence operator
c='He said,"I want to eat an apple"' #using traditional method
print(b,"Size of b is :",len(b))
print("\n")
print(c,"Size of c is :",len(c))
#multiline strings in python
#we can intialize multiline string by using three 
c='''Ramendra is a good boy
     Vinnet is also very good boy'''
print(c)
#looping in python
fruits=["Apple","Banana","Orange"]
for y in fruits:
    print(y)
