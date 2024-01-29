
def name(fname,mname="Kumar",lname="Singh"):
    print("Hello",fname,mname,lname)
name("Ramendra","Pratap","Yadav")
# def avgOfnumber(*numbers):
#     sum=0
#     for i in numbers:
#     #  sum=0
#      sum=numbers+i     
#      print("Avg is :",sum/len(numbers))
# avgOfnumber(1,10)        
def avgOfnumber(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum / len(numbers)

c=avgOfnumber(1, 10,15,20,25,30)
print(c)
