l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(9)
print(l)
l.sort(reverse=True)
print(l)
print(l.index(4))
print(l.count(1))
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") 
print(thislist)