from asyncio import futures


class Dog :
    def __init__(self,no_of_eyes,color):
        self.no_of_eyes = no_of_eyes
        self.color = color
    def bark(self):
        print("woof woof!")
    def pant(self):
        print("panting")


german_shepherd = Dog(no_of_eyes=2, color="grey")
dodger = Dog(no_of_eyes=1, color="white")
dobberman = Dog(2,"brown")
print(german_shepherd.color)
print(dodger.no_of_eyes)
print(dobberman.no_of_eyes, dobberman.color)
dobberman.color ="dark- brown"
print(dobberman.color)
dobberman.bark()
german_shepherd.pant()


