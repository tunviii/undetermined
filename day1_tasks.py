##Task 1:
"""name=input("Enter your name: ")
age=int(input("Enter your age: ")) #Defining datatype for each variable. If not defined, str datatype is taken by deafult.
height=float(input("Enter your height in m: "))
lang=input("Enter your favourite programming language: ")
year=int(input("Enter years of coding experience: "))
learn=bool(input("Are you currently learning python: "))
print("=== Personal Information ===")
print(f"Name: {name}") #Using fstrings for printing variables
print(type(name))
print(f"Age: {age}")
print(type(age))
print(f"Height: {height}")
print(type(height))
print(f"Fave programming language: {lang}")
print(type(lang))
print(f"Coding epxperience in years: {year}")
print(type(year))
print(f"Currently learning python? {learn}")
print(type(learn))"""

##Task 2: 
"""pname="Wireless Mouse"
price=29.99
quantity=5
dper=10
total=price*quantity
discam=(total*dper/100)
finam=total-discam
print("=== Product Info ===")
print(f"Product name: {pname}")
print(f"Unit price: {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {total}")
print(f"Discount percentage and amount: {dper}, {discam}")
print(f"Final Price: {finam}")"""

##Task 3:
"""fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
byear=int(input("Enter your birth year: "))
age=2026-byear
fnum=int(input("Enter your favourite number: "))
print("=== User Info ===")
print(f"Full Name: {fname} {lname}")
print(f"Age: {age}")
print(f"Number: {2*fnum}")"""

##Task 4:
values=[0,1,"", "hello", [], [1,2,3], None, True, False, "False"]
print("Truthy/Falsy check")
print("-"*30)
for value in values:
    if value:
        print(f"{repr(value)} -> Truthy")
    else:
        print(f"{repr(value)} -> Falsy")

##Task 5:
"""num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
print(f"Addition: {num1+num2}")
print(f"Subtraction: {num1-num2}")
print(f"Multiplication: {num1*num2}")
print(f"Division: {num1/num2}")
print(f"Floor Division: {num1//num2}")
print(f"Modulo: {num1%num2}")
print(f"Exponentiation: {num1**num2}")"""

##Task 6:
"""age=int(input("Enter your age: "))
lic=bool(input("Do you have a license? "))
if age>=18 and lic==True:
    print("Can drive.")

if age>=65:
    print("Is senior citizen.")

if age>=13 and age<=20:
    print("Is teenager.")

if age>=18:
    print("Can vote.")"""