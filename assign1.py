class person ():
    def __init__(self,name,yob,height,weight):
        self.name = name
        self.yob = yob
        self.height = height
        self.weight = weight
    def BMI(self) :
        BMI = self.weight/(self.height*self.height)
    def age(self):
        age = 2022-self.yob
    def details(self):
        print("my name is", self.name, "and my age is", self.age, "and my BMI is",self.BMI)
class student (person):
    def __init__(self,subject,clas):
        self.subject = subject
        self.clas = clas
class teacher (person):
    def __init__(self,subject,salary):
        self.subject = subject
        self.salary = salary
Moses = person("moses","2010",40,6)





