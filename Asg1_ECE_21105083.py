# Question 1: Write a Python program to find average of three numbers entered by the user.
# imput
print('             *** Question 1 ***')
first_number=int(input('Enter first number: '))
second_number=int(input('Enter second number: '))
third_number=int(input('Enter third number: '))

# Calculations
average=(first_number+second_number+third_number)/3

print('Average of three numbers is ',average)


#Question 2:Write a python program to compute a person's income tax. Assume following tax laws...
print('             *** Question 2 ***')

Gross_income = int(input('Enter The Gross Income: '))
dependent_deduction = int(input('Enter the number of Dependents: '))

# Calculations
taxable_income = Gross_income - 10000 - (dependent_deduction*3000)
tax = taxable_income*20/100

print('The total income tak to be paid is $',tax)

# Question 3: Write a python program to store different data type values into a list
print('              *** Question 3 ***')

sid = int(input('Enter Student ID: '))
name = input('Enter your name: ')
gender = input('Enter your Gender (M, F, U): ').upper()
course = input('Enter the Course for which u registered: ')
cgpa = float(input('Enter your CGPA: '))

Student = [sid,name,gender,course,cgpa]
print(Student)

# Question 4: Write a python program to enter marks of 5 students into a list and display them in sorted manner
print('              *** Question 4 ***')

Marks1=float(input('Enter marks scored in Subject 1'))
Marks2=float(input('Enter marks scored in Subject 2'))
Marks3=float(input('Enter marks scored in Subject 3'))
Marks4=float(input('Enter marks scored in Subject 4'))
Marks5=float(input('Enter marks scored in Subject 5'))

Marks_list=[Marks1,Marks2,Marks3,Marks4,Marks5]
Marks_list.sort()   #Sorting of list
print(Marks_list)

# Question 5: List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('              *** Question 5-a ***')

# Part A: Write a Python program to print a specified list after removing 4th element

input_list = ['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
print("Input list: ",input_list)

# to Remove 4th Element from the list.
input_list.pop(3)
print('Modified list: ',input_list)

print()

# Part b: Remove Black,Pink and add purple in them using 1 line of code
 
print('              *** Question 5-b ***')
input_listb = ['Red','Green', 'White', 'Black', 'Pink', 'Yellow']

# Manipulations on string
input_listb.remove('Black');
input_listb.remove('Pink');
input_listb.insert(3,'Purple');

print(input_listb)