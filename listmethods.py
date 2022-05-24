fruits = ["banana", "avocado", "pineapple", "apple","orange"]
fruits_2 =["cherry","tomato"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)
my_fruits = fruits.pop(1)
print(fruits)
print(my_fruits)
fruits_3 = fruits + fruits_2
print(fruits_3)
fruits_2.clear()
print(fruits_2)
fruits_4 = ("apple", "orange", "banana")
print(fruits_4)
print(fruits_4[1])
new_list = list(fruits_4)
new_list.append("tomato")
fruits_4 = tuple(new_list)
print(fruits_4)
fruits_5 = {"apple", "oranges","oranges" , "oranges"}
print(fruits_5)