numbers = [5,150,400,450,150,15,20,20,56,450,78]
newlist =[]
for num in numbers:
    if(num not in  newlist):
        newlist.append(num)     
#newlist=[num for num in numbers if num not in newlist]
newlist.sort()
print(newlist)
