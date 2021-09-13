x=1  #int
y=2.5 #float
name ="Tan Vuu" #String
is_hot=False #boolean



a,b,c,d=(1, 2.5,"hello world",True)



a=str(a)
b=int(b)
# print(b,type(b))

# print("hello my name is {name} and i'm {age}".format(name=name,age=x))
# print(f"hello my name is {name} and i'm {x}")
# print(f"hello my name is {name} and i'm {y}")
s="hello world"

# print(s.capitalize())




numbers=[1,2,3,4,5,6]

numbers2=list((1,2,3,9,4))
numbers2[0]=10


person={
    'name':"tanvuu",
    'age':10
}

# print(person,type(person))
person['phone']="0368510465"

person2=person.copy()
person2['email']="tanvuu998@gmail.com"
# print(person)


persons=[
    {"name":"tanvuu","age":21},
    {"name":"thuynga","age":20}
]
# print(persons[0]['name'])

def sayHello():
    print("hello world")
    print("hello 2")
    print("hello")
    return 2
# sayHello()
# print(sayHello())
list=["hello",1,2,False]

myList=[9,6,2,10,88,22]
myList.sort(reverse=True)
# print(myList)


def sum(num1,num2):
    return num1+num2
getSum=lambda num1,num2:num1+num2

getMultiple=lambda num1,num2:num1*num2
# print(getMultiple(20,25))
x=10
y=5
def compare(x,y):
    if(x>y):
        print(y)
    else:
        print(x)
for item in myList:
    print(item)

myList=["a",'b',"c"]
for i in range(len(myList)):
    print(myList[i])


while i<len(myList):
    print(myList[i])
    i+=1


def my_function(**kid):
    print("my nam is "+kid["name"])
my_function(fullname="tanvuu",name="tan")