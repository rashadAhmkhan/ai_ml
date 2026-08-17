"""
AIML Course - Python Fundamentals & String Operations
This script contains all foundational code from the course materials.
"""

import math #[cite: 1]

# ==========================================
# PART 1: Python Fundamentals[cite: 1]
# ==========================================

print("\n--- Hello World & Quotes ---")
# Simple print statements to communicate output[cite: 1]
print("Hello, World!") #[cite: 1]
print("Welcome to Python!") #[cite: 1]

# Three ways to handle quotes inside strings[cite: 1]
print("Hi \"Python\"") # Escape character[cite: 1]
print('Hi "Python"') # Mixed quotes[cite: 1]
print("""Hi 
Python""") # Triple quotes for line breaks[cite: 1]

print("\n--- Variables & Dynamic Typing ---")
# A variable points to an object stored in memory; it doesn't contain the value itself[cite: 1]
name = "Jaskirat Singh" #[cite: 1]
print(name) #[cite: 1]

name = "Hamza Ali Mazar" #[cite: 1]
print(name) #[cite: 1]

# Python is dynamically typed, meaning the type can change during reassignment[cite: 1]
x = "Hello" #[cite: 1]
print(type(x)) #[cite: 1]

x = 100 #[cite: 1]
print(type(x)) #[cite: 1]

# Reassigning and computing line-by-line[cite: 1]
a = 10 #[cite: 1]
b = 20 #[cite: 1]
c = a + b #[cite: 1]
print(c) #[cite: 1]

print("\n--- Datatypes: Primitives vs Collections ---")
# Primitive values[cite: 1]
a = 10           # int[cite: 1]
b = "Manish"     # str[cite: 1]
c = 3.14         # float[cite: 1]
d = True         # bool[cite: 1]
e = None         # NoneType[cite: 1]

# Collections[cite: 1]
nums = [1, 2, 3] # list[cite: 1]
pair = (1, 2)    # tuple[cite: 1]
uniq = {1, 2, 3} # set[cite: 1]
info = {"a": 1}  # dict[cite: 1]
print(type(nums)) #[cite: 1]

print("\n--- Input, Output & Practical Examples ---")
# Using inputs and casting them to integers[cite: 1]
# Note: Commented out the inputs so the script runs straight through without pausing, 
# but this is how we prompt the user as shown in the slides[cite: 1].
# user_name = input("Enter your name: ") 
# print("Hello, " + user_name)
# age = int(input("Your age: ")) 
# print("Next year: ", age + 1)

# Calculating revenue[cite: 1]
total_qty = 35 #[cite: 1]
price = 100 #[cite: 1]
revenue = price * total_qty #[cite: 1]
print(revenue) #[cite: 1]

# Multi-line printing layout[cite: 1]
print("""Learning path:
-Python Basics
-Data Engineering
-AI Engineering""") #[cite: 1]

print("\n--- Functions vs Methods ---")
# Built-in vs External vs User-defined[cite: 1]
print(math.sqrt(16)) # External[cite: 1]

def greet(name): # User-defined[cite: 1]
    return "Hi " + name #[cite: 1]
print(greet("Alex")) #[cite: 1]

# Standalone functions vs Class-bound methods[cite: 1]
text = "Manish" #[cite: 1]
num = 99 #[cite: 1]
print(type(text)) #[cite: 1]
print(len(text)) #[cite: 1]
print(text.upper()) #[cite: 1]


# ==========================================
# PART 2: String Datatypes & Methods[cite: 2]
# ==========================================

print("\n--- Cleaner Code with f-Strings ---")
# Using f-strings to avoid hardcoded duplicated values[cite: 2]
name = "Vardaan" #[cite: 2]
language = "Python" #[cite: 2]
print(f"My name is {name}") #[cite: 2]
print(f"{name} loves {language}") #[cite: 2]

print("\n--- Escape Sequences ---")
print("Line1\nLine2") # new line[cite: 2]
print("Hi\tEveryone") # tab spacing[cite: 2]
print("Path: C:\\Users") # literal backslash[cite: 2]
print("She said \"Hi\"") # quotes inside quotes[cite: 2]

print("\n--- String Types & Math ---")
# Inspecting and measuring strings[cite: 2]
age_str = 24 #[cite: 2]
print("Age: " + str(age_str)) #[cite: 2]

password = "mypassword" #[cite: 2]
print(len(password)) #[cite: 2]

text = "Py Py Py" #[cite: 2]
print(text.count("Py")) #[cite: 2]

print("\n--- String Transformations ---")
# Reshaping strings[cite: 2]
date = "2026/05/10" #[cite: 2]
print(date.replace("/", "-")) #[cite: 2]

first = "Manish" #[cite: 2]
last = "Raj" #[cite: 2]
print(first + " " + last) # Concatenation[cite: 2]

csv = "Manish,25,USA" #[cite: 2]
print(csv.split(",")) # Break into a list[cite: 2]
print("*" * 20) # Repeat n times[cite: 2]

print("\n--- Slicing & Indexing ---")
# Extracting specific parts of a string[cite: 2]
code = "Manish-25" #[cite: 2]
print(code[0]) # Single char (0-indexed)[cite: 2]
print(code[-1]) # Negative index counts from right[cite: 2]
print(code[0:6]) # Substring, end exclusive[cite: 2]
print(code[-2:]) #[cite: 2]

date_str = "2026-05-20" #[cite: 2]
print(date_str[0:4], date_str[5:7], date_str[8:10]) #[cite: 2]
print(date_str[::-1]) # With a stride (reversing)[cite: 2]

print("\n--- String Cleaning ---")
# Removing whitespace and normalizing case[cite: 2]
dirty_name = "  Manish  " #[cite: 2]
print(dirty_name.strip()) #[cite: 2]
print(dirty_name.lstrip()) #[cite: 2]
print(dirty_name.rstrip()) #[cite: 2]
print("###Manish###".strip("#")) # Remove specific characters[cite: 2]

search = "EMAIL" #[cite: 2]
data = "  email  " #[cite: 2]
# Chaining methods for reliable comparison[cite: 2]
print(search.lower() == data.strip().lower()) #[cite: 2]

print("\n--- String Search ---")
# Finding and matching substrings[cite: 2]
phone = "+91-12345" #[cite: 2]
print(phone.startswith("+91")) #[cite: 2]

file = "data_backup.csv" #[cite: 2]
print(file.endswith(".csv")) #[cite: 2]

email = "Manish@gmail.com" #[cite: 2]
print(email.find("@")) # Returns index of first match[cite: 2]
print("@" in email) # Boolean substring check[cite: 2]

print("\n--- Validate, Join, Format ---")
# Character checks and joining lists[cite: 2]
print("123".isnumeric()) #[cite: 2]
print("abc".isalpha()) #[cite: 2]

parts = ["2026", "05", "20"] #[cite: 2]
print("-".join(parts)) # Opposite of split()[cite: 2]

print("Hi, {}. Order {}".format("Sam", 123)) # Older alternative to f-strings[cite: 2]
print("42".zfill(5)) # Pad with leading zeros[cite: 2]
