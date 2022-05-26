# dictionaries in python
mydict = {
    "book" : "dynamics",
    "publisher" :"longhorn",
    "year" : 2001,
    "authors" : ["John","Mike","Ike"]
            }
# accesing item
x = mydict["year"]
print(x)
#accesing using get()
y = mydict.get("year")
print(y)
# all keys
x = mydict.keys()
print(x)
x = mydict.values()
print (x)
# printing all items in a dictionary
x = mydict.items()
print(x)
# checking if key exists
if "publisher" in mydict:
    print("publisher is one of the keys")
print(len(mydict))
