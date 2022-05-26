try:
    value = int(input("enter a number"))
    print(value)
except ValueError :
    print("invalid number entred")
except ZeroDivisionError :
    print("divided by zero")