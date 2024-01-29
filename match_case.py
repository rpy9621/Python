#match case in python
age=int(input("Enter age : "))
match age:
    case 18:
        print("Ellible for vote \n")
        print("Elligible for drive")
    case 60:
        print("Senier Citizen")
        print("Age is equal or more than 60")
    case _:
        print("\"Happy Happy Happy\"")