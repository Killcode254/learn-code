file = open("roles.txt","r")
w = file.read()
print(w)
file = open("roles.txt","a")
w = file.write("\n I love python")
print(w)
file.close