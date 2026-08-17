#Built-In numeric types

x = 10 
y = 2.73
z = 2 + 4j

print(type(x))
print(type(y))
print(type(z))


#operations
a = 10
b = 3


print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns float
print(a//b) #returns int
print(a%b)
print(a**b)


#Comparison and Logical Operators

##Comparison
x,y = 10,3

print(x == y)
print(x != y)
print(x <= y)
print(x >= y)

##logical
print(x > 5 and y < 5)
print(x < 5 or y > 0)
print(not(x == y))

#Rounding(MAth Module)
import math

#floor
print(math.floor(3.9))  # Output: 3
print(math.floor(-3.1)) # Output: -4

#ceil
print(math.ceil(3.1))   # Output: 4
print(math.ceil(-3.9))  # Output: -3

#trunc
print(math.trunc(3.9))  # Output: 3
print(math.trunc(-3.9)) # Output: -3

#round
print(round(2.55423, 2))


#Data Structures

num = [20,30,40]

names = ["Obama", "JD", "Musk"]

status = [True, False, True]

data = ["Turing", 30, False]
print(data)
print(data[1])


print("Appned in data")

data.append(2.3334)
print(data)

print("After removing and popping")
data.pop()
data.remove(30)
print(data)


#len() function

##len() is a universal function that returs the length of an object
a = "This is a string"
b = [23,22,3,31,12,111,2]

print("\n ===============================")

print("String: " , a)
print("List: ", b)
print(f'length of string: {len(a)}')
print(f'Length of list: {len(b)}')


#sort()

print("Sorting list")
b.sort()
print(b)

#reverse()

print("Reversing String")
b.reverse()
print(b)
