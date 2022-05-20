print("WELCOME")
print("Choose A,B,C or D")
print("Use uppercase letters")
function = input("(A)circle or (B)rectangle or (C)square or (D)triangle: ")
if function == "A":
    pi = float(22/7)
    r = float(input("input the radius"))
    area = pi*(r*r)
    print("the area of the circle equals", area)
elif function == "B":
    l = float(input("input length"))
    w = float(input("input width"))
    area = l*w
    print("the area of the rectangle equals", area)
elif function == "C":
    s1 = float(input("input value of side"))
    area = s1*s1
    print("the area of the square equals", area)
elif function == "D":
    x = float(0.5)
    b = float(input("input base length"))
    h = float(input("input height"))
    area = x*b*h
    print("the area of the triangle equals", area)
else:
    print("Error please input a valid choice and use upper case letters")
    print("Restart the program and try again")

print("Thank you")





    
    


