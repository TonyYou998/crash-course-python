# Chúng ta có một list như sau:
# my_list = ["Hoc sinh", 1, False,"Sinh vien",2, True]

# 1 Điền cú pháp chính xác để in ra phần tử thứ hai của list
# Bài tập 2: Thay đổi giá trị “Sinh vien” thành “Giang vien”
# • Bài tập 3: Dùng phương thức insert() để thêm vào “Giang vien” như là đối tượng 
# thứ 2 trong list
# • Bài tập 4: Sử dụng chỉ mục âm để in ra phần tử cuối cùng của list
# • Bài tập 5: Điền cú pháp chính xác để in ra phần tử thứ 3, 4, 5






my_list =["Hoc sinh", 1, False,"Sinh vien",2, True]
# cau 1
print(my_list[1])
# cau 2
my_list[3]="Giang vien"
print(my_list)

# cau 3
my_list.insert(1,"Giang vien")
print(my_list)
# cau 4
print(my_list[-1])
# cau 5
print(my_list[2:5])



# tìm số nhỏ nhất,lớn nhất,tổng trong list

# arr=[1,8,9,20,30,6]

def findMin(arr):
    min=arr[0]
    for i in range(len(arr)):
      
        if(arr[i]<min):
            min=arr[i]
    return min

def findMax(arr):
    max=arr[0]
    for x in range(len(arr)):
        if(arr[x]>max):
            max=arr[x]
    return max

def sum(numbers):
    sum=0
    for x in numbers:
        sum+=x
    return sum


print("so nho nhat la:",findMin([2,-10,66,-99,34]))
print("so lon nhat la:",findMax([2,-10,66,-99,34]))
print("tong la :",sum([2,-10,66,-99,34]))
# taọ class animal có các thuộc tính name,age
# class dog kế thừ class animal có thêm thuộc tính type=dog và phương thức printInfo sẽ in ra name,age và type


class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)    
        self.type="dog"
    def printInfo(self):
        print("name:",self.name)
        print("age:",self.age)
        print("type:",self.type)

toto=Dog("toto",7)

toto.printInfo()

        



    

