# multiple line strings
from codecs import BOM_BE


msg = """QEHUTXZKJ748 Confirmed
          you have received 73777
          from
           name"""
print(msg)
city = "nairobi"
print(city.upper())
uni = "JKUAT"
print(uni.lower())
fruit = "avocado"
print(fruit[:2])
print(fruit[5:])
print(fruit[:-1])
print(fruit[-3:])
#strip removes spaces btwn the words
f_name = " Bob Afwata"
print(f_name.strip())
print(f_name)
f_name = "bob"
l_name = "afwata"
full_name = (f_name+l_name)

print(full_name)
print(len(full_name))
word = "abracadabra"
print(len(word))
x = 100
print(str(x))