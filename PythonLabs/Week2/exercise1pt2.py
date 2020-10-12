# a
temp = int(input("type temperature in celsius to convert to Fahrenheit: "))
print ("Fahrenheit = " + str((temp * 9/5) +32))


# b
import math
pi = math.pi
radiusci = int(input("type radius of a circle: "))
print("area of circle = " + str(pi * radiusci * radiusci))
print("circumferance of circle = " + str(2 * pi * radiusci))


# c
radiuss = int(input("type radius of a sphere: "))
print("area of a sphere = " + str(4* pi * radiuss * radiuss))


# d
radiuscy = int(input("type radius of a cylinder: "))
heightcy = int(input("type height of a cylinder: "))
print("area of a cylinder = " + str((2 * pi * radiuscy * radiuscy) + (2 * pi * radiuscy * heightcy)))


# e
firstname = input("type your firstname: ")
surname = input("type your surname: ")
print(firstname[0] + " " + surname[0])


#f
age = int(input("type in your age: "))
print(age > 17)

