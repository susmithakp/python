a={30,"cake","pizza","Biryani",40,50}
b={30,"cake","blueberries",46,78}
#a.update(b) removes duplicate values 
#a.intersection_update(b) keeps duplicate values 
#c=a.intersection_update(b) keeps duplicate values in a new set
#a.symmetric_difference_update(b)
c=a.symmetric_difference(b)
print(c)