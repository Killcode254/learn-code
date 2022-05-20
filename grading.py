grade = int(input("write student score"))
if grade > 80 and grade <=100:
    print("student got an A")
elif grade >= 70 and grade <80:
    print("student got a B")
elif grade >= 60 and grade <70:
    print("student got a C")
elif grade >= 50 and grade <60:
    print("student got a D")
elif grade <50:
    print("student got an E")
else:
    print("wrong marks input")