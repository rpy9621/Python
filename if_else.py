#if else condition on python
age=float(input("Enter your age to check that you are elligible for vote or not :\n"))
if age>=18:
    print("Elligible for vote & your age is :",age,"\n")
    print("You can drive")
else:
    print("Not elligible due to age limit :",age,"\n")
    print("You can'nt drive")