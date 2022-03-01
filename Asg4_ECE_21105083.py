###################################################################################################################


print("*** Question 1 ***\n")

def towerOfHanoi(n , source, destination, auxiliary): # Creating function for tower of hanoi
    step=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    towerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    towerOfHanoi(n-1, auxiliary, destination, source)

# taking input from the user
total_discs=int(input("Enter number of disk in tower of Hanoi:"))

print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks in order are given below:\n")

#Using the function of tower of hanoi
towerOfHanoi(total_discs,"Source","Destination","Auxiliary")


##################################################################################################################


print("\n*** Question 2 ***\n")


# Recuesive Approach
print("The Pascal's Triangle using recursive approach:\n")


def print_next_row(list1, row): # function to return next row of elements of pascal's triangle
    counter1 = 0
    counter2 = 1
    list = []
    for counter1 in range(row - 1):
        list.append(list1[counter1] + list1[counter2])
        counter1 = counter1 + 1
        counter2 = counter2 + 1
    list.insert(0, 1)
    list.append(1)
    return (list)


def pascals_triangle(row_number,list1,row): # Function to print pascal's triangle
    if row_number==0:
        return
    else:
        next=print_next_row(list1,row)
        liste=next.copy()
        listp=list(map(str,liste))
        p="  ".join(listp)
        print("{s:^100}".format(s=p))
        pascals_triangle(row_number-1,next,row+1)

row_number=int(input("Enter number of rows in Pascle's Triangle:"))
#Alligning the pascle's triangle in triangular form using string formatting and printing it
if row_number==1:
    print("{a:^100}".format(a="1"))
elif row_number==2:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1 1"))
else:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1  1"))
    pascals_triangle(row_number-2,[1,1],2)


print("\nThe Pascal's Triangle using Iterative approach is:\n")

row=int(input("Enter number of rows:")) # taking input of rows

def print_next_row(list1, row): # forming fuction to return next row of pascal triangle
    counter1 = 0
    counter2 = 1
    next_row = []
    for counter1 in range(row - 1):
        next_row.append(list1[counter1] + list1[counter2])
        counter1 = counter1 + 1
        counter2 = counter2 + 1
    next_row.insert(0, 1)
    next_row.append(1)
    return (next_row)


def print_pascal_triangle(rows): # function to print all rows using previous function
    if rows == 1:
        print("{a:^100}".format(a="1"))
    elif rows == 2:
        print("{b:^100}".format(b="1"))
        print("{b:^100}".format(b="1 1"))
    else:
        f = "{p:^100}".format(p=1)
        print(f)
        f = "{p:^100}".format(p="1  1")
        print(f)
        l1 = [1, 1]
        row = 2
        for i in range(rows - 2):
            v = print_next_row(l1, row)
            v2 = v.copy()
            v2 = list(map(str, v2))
            n = rows
            k = "  ".join(v2)
            f = "{p:^100}".format(p=k)
            print(f)
            row = row + 1
            l1 = v
print_pascal_triangle(row)


##################################################################################################################


print("\n*** Question 3 ***\n")


#Taking input from the user
from math import remainder


number1=int(input("\nEnter an Integer:"))
number2=int(input("Enter another Integer:"))


list1=list(divmod(number1,number2))

#a1=Quotient
quotient=list1[0]
#a2=Remainder
remainder=list1[1]

#printing the quotient and remainder
print(f"\nThe quotient when {number1} is divided by {number2} is {quotient}.")
print(f"The remainder when {number1} is divided by {number2} is {remainder}.")

######################################## Question 3.a #########################################################

print("\nQuestion 3.a")
check_call=callable(divmod(number1,number2))
if check_call==True:
    print(f"Function is callable")
if check_call==False:
    print(f"Function is not-callable")

######################################## Question 3.b #########################################################

print("\nQuestion 3.b")

listv=[quotient,remainder]
zero=False
if zero in listv:
    zero=True
else:
    zero=False

if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are non-zero")

######################################## Question 3.c #########################################################

print("\nQuestion 3.c")

listr=[quotient,remainder]
for index in range (4,7):
    listr.append(index)
print(f"Appended (4,5,6) in the values ({quotient},{remainder})")
listv2=[]
#adding number > 4 from listr to listv2
for index in listr:
    if index>4:
        listv2.append(index)

#copying listv2 but in string form

listv3=list(map(str,listv2))

v=",".join(listv3)
print(f"Values greater than 4 is {v}")

######################################## Question 3.d #########################################################

print("\nQuestion 3.d")
set1={1,2}
set1.clear()

#adding above result in set datatype
for elements in listv2:
    set1.add(elements)
print("Above result in set form is shown below:")
print(set1)

######################################## Question 3.e #########################################################

print("\nQuestion 3.e")

#Making set1 immutable
frozenset(set1)
print("The above set is now immutable.")

######################################## Question 3.f #########################################################

print("\nQuestion 3.f")
print(f"Maximum value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")


print("\n*** Question 4 ***\n")

class student: # defining a class named student

    #using constructor to set value to class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    #defing print function
    def print_intro(self):
        print(f"Hello, My name is {self.name} and my SID is {self.roll_no}")

    #calling destructor
    def __del__(self):
        print("Destructor Called")

vasu=student("Vasu",21105083) # creating vasu object of class student
vasu.print_intro()
del vasu

print("\n*** Question 5 ***\n")

class employees: # defining a class employee


    def __init__(self,name,salary): # using constructors to initialise member variables
        self.name=name
        self.salary=salary

    def print_details(self):
        print(f"employee name is {self.name} and salary is {self.salary} ")

# setting employee details
employee1=employees("Mehak",40000)
employee2=employees("Ashok",50000)
employee3=employees("Viren",60000)

# printing employee detail
employee1.print_details()
employee2.print_details()
employee3.print_details()

# updating Mehak's salary to 70000
print("\nQuestion 5.a\n")
employee1.salary=70000
print("Mehak salary Updated to 70000")
employee1.print_details()

# Deleting Viren's data
print("\nQuestion 5.b")
del employee3
print("Employee Viren's data has been removed.")

print("\n*** Question 6 ***\n")


gap="\t"*5
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.index1. anagram
def anagram(word1,word2):

    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()

    #form empty list to store letters of words
    list_1=[]
    list_2=[]
    for index1 in word1:
        list_1.append(index1)
    for index2 in word2:
        list_2.append(index2)

    # sorting the list alphabetically
    list_1.sort()
    list_2.sort()

    if list_1==list_2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\n enter name of player 1:"))
player2=str(input("enter name of player 2:"))

#taking words spoken by written
word_player1=str(input(f"\nenter word by {player1}:"))
word_player2=str(input(f"enter word by {player2}:"))

#using anagram function
result=anagram(word_player1,word_player2)

#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
