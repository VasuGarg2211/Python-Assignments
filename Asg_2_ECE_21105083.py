# Question 1

print("       Question 1")
input_string = "Python is a case sensitive language" # Given in the question

# Part 1.a--> Finding length of input string
print("1.a--> Length of the input string is:",len(input_string))

# Part 1.b--> Reversing the string
print("1.b--> Reverse of input string is:",input_string[::-1]) 

# Part 1.c--> Slicing the string and storing it in new variable.
sliced_string = input_string[10:26]   
print("1.c--> Sliced string is:",sliced_string)

# Part 1.d--> Replacing a part of the string
replaced_string=input_string.replace("a case sensitive", "object oriented") 
print("1.d--> String after replacing is:",replaced_string)

# Part 1.e--> Finding the index of a substring
print("1.e--> Index of substring \"a\" is:",input_string.index("a")) 

# Part 1.f--> Removing " " from input string
print("1.f--> String after removing \" \" is:",input_string.replace(" ","") ) 

print("\n")

# Question 2
print("         Question 2")
# initialising values as per question
name="Vasuman"
SID=21105083
department="ECE"
CGPA=9.5

print("Hey, %s Here!"%name)
print("My SID is %d"%SID)
print("I am from %s department and my CGPA is %f"%(department,CGPA))

print("\n")

# Question 3

print("         Question 3")
# initialising values as per question
a=56
b=10
# Calculating
print("3.a--> a&b=",a&b)
print("3.b--> a|b=",a|b)
print("3.c--> a^b=",a^b)

# Left shift both a and b with 2 bits.
print("3.d--> a<<2=",a<<2,"and b<<2=",b<<2)
# Right shift a with 2 bits and b with 4 bits.
print("3.e--> a>>2=",a>>2,"and b>>4=",b>>4)

# Question 4
print("         Question 4")

# Taking input
first=int(input("Enter first number:"))
second=int(input("Enter second number:"))
third=int(input("Enter third number:"))

if(first>second):
    if(first>third):
        max=first
    else:
        max=third
else:
    if(second>third):
        max=second
    else:
        max=third

print("greatest of three numbers is",max)

print("\n")

# Question 5
print("         Question 5")
string=input("Enter a string:")
if "name" in string:
    print("Yes")
else:
    print("No")

print("\n")

# Question 6
print("         Question 6")

# taking input of lengths of triangle
first=int(input("Enter first length:")) 
second=int(input("Enter second length:"))
third=int(input("Enter third length:"))

# checking condition for triangle.
if first+second>third and first+third>second and second+third>first:
    print("Yes")
else:
    print("No")