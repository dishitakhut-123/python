class Person:
    def __init__(self,id,name):
        print("object created!")
        self.id=id
        self.name=name
class Student(Person):
    def __init__(self,id,name,sem,mark1,mark2):
        Person.__init__(self,id,name)
        self.sem=sem
        self.mark1=mark1
        self.mark2=mark2
    def avrmarks(self):
        total=self.mark1+self.mark2
        avg=total/2
        print("Average marks",avg)
        print()
    def getdata(self):
        print("Id",self.id)
        print("name",self.name)
        print("sem",self.sem)
        print("marks1",self.mark1)
        print("mark2",self.mark2)
    def __del__(self):
        print("object destroyed")
x=Student(1,"swayam",2,60,60)
print(x.getdata())
print(x.avrmarks())
y=Student(2,"swayam",1,80,90)
y.getdata()
y.avrmarks()

