other_list = []
my_list = [1, 3 , 75, 854, 7654, 85, 9]
for x in my_list:
    if x%2 == 0:
        other_list.append(x)
print(other_list)
my_list = [1, 3 , 75, 854, 7654, 85, 9]
other_list = [x for x in my_list if x%2 == 0]
print(other_list)


