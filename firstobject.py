


from os import name


class first:
    def __init__(self,name,age ):
        self.name=name
        self.age=age
        print("I am " +name )
        print("I am " +str(age)+ " years old")
    def getName(self,name):
        name=self.name
        print("my name is ", name)
a=first("susmitha",37)
a.getName(name)

    
