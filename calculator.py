no1 = float(input("input the first number"))
no2 =float(input("input the second number"))
function = input("input the function")
if function == "+":
   p = no1+no2
   print(p)
elif function == "-":
    p = no1-no2
    print(p)
elif function == "*":
    p = no1*no2
    print(p)
elif function == "/":
    p = no1/no2
    print(p)
else :
    print("use a valid function")
    print("Rerun the program and try again")