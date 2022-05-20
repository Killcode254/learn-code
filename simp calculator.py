no1 = float(input("input the first number"))
no2 = float(input("input the second number"))
function = input("input the function")
p = 0
if function == "+":
   p = no1+no2
elif function == "-":
    p = no1-no2
elif function == "*":
    p = no1*no2
elif function == "/":
    p = no1/no2
elif function == "%":
    p = no1%no2
else:
    print("use a valid function")
    print("Rerun the program and try again")
print("your answer is equal to", p)
