'''in a python program if there is any error occured in our program so we want that our program is not going to terminate and from that our rest of code will work as their scheduled task so in this case we use exception handling in python and they are mainly three:try,except and finally and try is used to check the occurancy of error and except show what the error occured in our code and finally use if we want to print something '''
# ram={'Ramennrda',"Rana_Pratap",'Ritesh',"Prashant_Kumar"}
# try:
#     if ana in ram:
#         print('True')
# except :
#     print('False')
# finally:
#     print("Ana is present in above name but w are unable to find")

a=input('Enter the Number : ')
try:
    print('Multiplication of',a,'is :')
    for i in range(1,11):
        print(int(a),'*',int(i),'=',int(a)*int(i))
except:
    print('Invalid Input')
finally:
    print('MY NAME IS RAMENDRA')
