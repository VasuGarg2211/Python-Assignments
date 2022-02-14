
###################################### Question 1 #####################################################################

from ast import Num
from tokenize import Number


print("\n*** Question 1 ***\n")
# Take Input from the user.
input_string = input("Enter a string: ")
input_string = input_string.lower().strip()
index = 0

dict = {} # Empty dictionary to store element and eliminating common words

# Checking the input_string
if " " not in input_string :
     # Searching for common elements
     while index < len(input_string) :
          count1 = 0
          index2 = 0
          while index2 < len(input_string) :
               if input_string[index] == input_string[index2]:
                    count1 = count1 + 1
                    index2 = index2 + 1
               else :
                    index2 = index2 + 1
          dict[f"{input_string[index]}"] = count1 # Storing in dictionary
          index = index + 1

else :
     # Storing words in a list
     list = str.split(input_string)
     # Searching for common words
     while index < len(list) :
          count1 = 0
          index2 = 0
          while index2 < len(list) :
               if list[index] == list[index2] :
                    count1 = count1 + 1
                    index2 = index2 + 1
               else :
                    index2 = index2 + 1
                    # Storing values in dictionary
          dict[f"{list[index]}"] = count1
          index = index + 1
# Printing the required output.
print("Individual letters/words and their frequencies: ")
for key,value in dict.items() :
    print(f"{key}--> {value}")

##################################### Question 2 #####################################################################
print("\n*** Question 2 ***\n")
print("Enter Valid date: ")

def check_leap_year(year) : # Function to check leap year
    if (year%400)==0 or ((year%100!=0) and (year%4==0)) :
        return True
    else :
        return False

#Taking input from user.

day = int(input("Enter Day in range [1-31]: "))
month = int(input("Enter Month in range [1-12]: "))
year = int(input("Enter Year in range [1800-2025]: "))

#Applying condition to check range of dates

if (day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025) :
    condition1 = False
else :
    condition1 = True

#Applying condition2 when day entered does not present in that month

month_31 = [1, 3, 5, 7, 9, 11]  # List containing month with 31 days
month_30 = [4, 6, 8, 10, 12]    # List containing month with 30 days

#if day==31 but it is not in that month

condition3 = (day==31 and (month in month_30))
# for day entered greater than 29 in month february i.e 2
condition4 = (day>29  and month==2)
# For invalid day in feb in Non-leap year
condition5 = (day==29 and (not check_leap_year(year)) and month==2)

if condition3 or condition4 or condition5 :
    condition2 = False
else :
    condition2 = True

# printing error when date entered is not correct
if condition3 :
    print(f"\nError\n{day} day is not present in month {month}")
elif condition4:
    print(f"\nError\n{day} day is not present in month {month}")
elif condition5:
    print(f"\nError\n{day} day is not present in month {month} as the year {year} in not leap year")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")

if (condition1==True and condition2==True) :
    month_31 = [1, 3, 5, 7, 9, 11]  #List containing month with 31 days
    month_30 = [4, 6, 8, 10, 12]    #List containing month with 30 days

    # For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1

    # For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1

    # for february month
    elif month == 2 :
        # If year is leap year
        if check_leap_year(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1

        # If year is not leap year
        elif check_leap_year(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1

    print(f"\nNext Date to entered date is: {day}:{month}:{year}")


####################################### Question 3 #####################################################################


print("\n*** Question 3 ***\n")

number_of_element=int(input("Enter number of elemnts : "))

list_1=[] # empty list to store numbers

for i in range(number_of_element):
    n=int(input("enter numbers of list: "))   #  Taking input and
    list_1.append(n)                        #  storing it in list

list_2=[]              # created empty list to store square of number
for i in list_1 :
    square_number = i * i
    list_2.append(square_number)

# FINAL OUTPUT
required_output=list(zip(list_1,list_2))
print("output is",required_output)

########################################### Question 4 ###################################################################


print("\n*** Question 4 ***\n")

Marks=int(input("Enter grade points:"))  #Taking input

#Forming a dictionary of statements
dic={10:"Your grade is A+\nOutstanding performance.",
     9:"Your grade is A\nExcellent performance.",
     8:"Your grade is B+\nVery Good performance.",
     7:"Your grade is B\nGood performance.",
     6:"Your grade is C+\nAverage performance.",
     5:"Your grade is C\nBelow Average performance.",
     4:"Your grade is D\nPoor performance."}

if 4<=Marks<=10:

    statement=dic.get(Marks) #Getting statements from dictionary

    print(statement)
else :
    print("\nError\nPlease enter grade in range [4,10]")


########################################### Question 5 ###################################################################

print("*** Question 5 ***")

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    count=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(list[count], end="")
            count=count+1
        column=column+1
    print("")



########################################### Question 6 ###################################################################
print("\n*** Question 6 ***\n")

dictionary ={}   # creating empty dictionary to store data

while True:
    input_choice = input("Enter Y to enter more data ,else enter N: ")



    if input_choice.upper() == 'Y':
        name = input("Enter your name :")
        sid = int(input("Enter your sid : "))
        dictionary[sid] = name
    elif input_choice.upper() == 'N':
        break
    else :
        print("Invalid choice")

#6.a
print("\n***** 6.a *****: \n",dictionary)

#6.b

print("\n***** 6.b *****\n")
print({i:j for i,j in sorted(dictionary.items(), key = lambda a:a[1])})   #Sorting using lambda function

#6.c

print("\n***** 6.c *****\n")
print({i:j for i,j in sorted(dictionary.items())})    # Sorting according to SID

#part (D) ---------
print("\n***** 6.d *****\n")
sid=int(input("Enter SID you want to search: "))
print("Name of student you searched is ",dictionary[sid])


########################################### Question 7 ###################################################################

print("*** Question 7 ***")
Number_of_terms=int(input("Number of terms of Fibonacci sequence you want to print: "))

if Number_of_terms<0:
    print("invalid input \nEnter a Positive number.")

sum=0 # To get sum of the series

def Fibonacci_Series(Number_of_terms):  # Fuunction to print Fibonacci series
    if Number_of_terms <= 1:
        return Number_of_terms
    else:
        return (Fibonacci_Series(Number_of_terms - 1) + Fibonacci_Series(Number_of_terms - 2))

for i in range(Number_of_terms):

    print(Fibonacci_Series(i))
    sum = sum + Fibonacci_Series(i)

if Number_of_terms==0:
    print(" average is 0")
elif Number_of_terms>0:
    print("the average of above series is ", sum / Number_of_terms)


########################################### Question 8 ###################################################################

print("\n*** Question 8 ***\n")

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# Creating a new set of all elements that are in Set1 or Set2 but not both.
print("Part 8.a")
set_partA=Set1^Set2
print(f"set with elements not common in both is {set_partA}")

#Create a new set of all elements that are in only one of the three sets Set1,Set2 and Set3
print("Part 8.b")
set_partB=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_partB}")

#Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3
print("Part 8.c")
set_partC = (Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_partC}")

# Create a new set of all integers in the range 1 to 10 that are not in Set1
print("Part 8.d")
set_partD=set()
for n in range(1,11):
    set_partD.add(n)
final_set_8D=set_partD- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {final_set_8D}")

#Create a new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.
print("Part 8.e")

set_partE=set()
for n in range(1,11):
    set_partE.add(n)
final_set_E=set_partE - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {final_set_E}")