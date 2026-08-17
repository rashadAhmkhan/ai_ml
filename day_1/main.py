#lists of list
list  = [[1,2,3,4], ["A","B"]] 

print(list)


name = input("Enter name")
print(name)

print("Lion Eats Grass")

a = 10
b = 30
print("Sum = ", a+b)

#product 
total_qty = 35
price = 60
revenue = price*total_qty
print(revenue)

#formatted string

print("""LEarning path:
PythonBasics
Data Engineering
AI engineering""")

#Read input as text

name = input("Enter Your Name: ")
age = int(input("enter Age: "))

print("Hello ", name)
print("You will be ", age+1, "next year")


#user-defined fucntions

def sum(a,b):
	return a+b

a= int(input("A= "))
b = int(input("B= "))
sum = sum(a,b)

print(f"Sum = {sum}")

#unicode error

#print("C:\Users\newsp\Downloads") #use \\ to prevent


#methods replace and split

date = "2026/05/10"
print(date.replace("/","-"))

csv = "Manish,25,USA"
print(csv.split(",")) #gives list of strings

#string navigation



first = "abhishek"; last= "kumar"
print(f"{first} {last}")

csv= "abhishek,20,India"
print(csv.split(","))

print("="*20)

code = "Abhishek-22"
print(code[0])
print(code[-1])
print(code[0:6])
print(code[-4:])
date= "2025-08-14"
print(date[0:4],date[5:7],date[-2:])

print(code[0:10:2])




#strip method

name = " JD Vance "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#strip characters
print("$JD Vance$".strip("$"))

#case sensitive cmparison

search = "EMAIL"
data = "email"
print(search.lower().strip() == data.lower().strip())


#find method
#Search Find & Match
phone="+48-456-7890"
print(phone.startswith("+48"))

file="data_backup.csv"
print(file.endswith(".csv"))

email="manish@gmail.com"
print(email.find("@"))
print("@" in email)

#use find() to slice dynamically
print(phone[phone.find("-")+1:])

#alpha numeric 
a = "a10"
print(a.isnumeric())
print(a.isalpha())
