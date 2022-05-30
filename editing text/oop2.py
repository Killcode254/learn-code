class person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print("my name is", self.name, "and my age is", self.age)
p1 = person("Felix", 22)
p1.details()
print(p1.name)