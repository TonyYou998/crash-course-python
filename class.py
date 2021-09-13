


# from _typeshed import Self


class MyClass:
    x=5


p1=MyClass()
print(p1.x)



class Person:
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
    def printMyName(self):
            print("my name is "+self.lastName)
        

# x=Person("vuu","tan")
# x.printMyName()

class Student(Person):
        def __init__(self, fname, lname,age,grade):
            super().__init__(fname, lname)
            self.age=age
            self.grade=grade
        def printInfo(self):
            print(f"grade:{self.grade} age:{self.age} ")


# x=Student("Tan","Vuu",21,3)
# x.printMyName()
# x.printInfo()


class Animal():
    def __init__(self,name,ability):
        self.name=name
        self.ability=ability
class Lion(Animal):
    def __init__(self, name, ability):
        super().__init__(name, ability)
        self.type="lion"
    def printInfo(self):
        print(f"name:{self.name} type:{self.type}")




            