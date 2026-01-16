print("="*30)
print("Welcome to Info Bank!")
print("="*30)
print("Please provide the following info: ")
fname=input("First Name: ")
lname=input("Last Name: ")
age=int(input("Age: "))
email=input("Email: ")
phone=int(input("Phone no: "))
city=input("City: ")
lang=int(input("No. of programming languages you know: "))
flang=input("What is your favourite progrmaming language? ")
exp=int(input("Years of coding experience: "))
student=bool(input("Are you a student? "))
birth=2026-age
print("="*30)
print("User Info Summary")
print("="*30)
print(f"Name: {fname} {lname}")
print(f"Age: {age} years old")
print(f"Birth Year: {birth}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"City: {city}")
print("="*30)
print("Programming experience: ")
print("="*30)
print(f"No. of programming languages known: {lang}")
print(f"Years of coding experience: {exp}")
if exp>0:
    avg=lang/exp
if exp<1:
    print("Experience Level: Beginner")
if exp>1 and exp<3:
    print("Experience Level: Intermediate")
if exp>3:
    print("Experience Level: Advanced")
print(f"Average Languages learnt per year: {avg}")
print(f"Student Status: {student}")
print("Keep up the good work!")
print("="*30)



