#Attribute Error

try:
    n="deepesh"
    n.remove("d")
except AttributeError:
    print(" AttributeError")

#ValueError

try:
    n=int("deepesh")
    print(n)
except ValueError:
    print("ValueError")


#Type error

try:
    n="deepesh"
    c=10+n
except TypeError:
    print("type error")
