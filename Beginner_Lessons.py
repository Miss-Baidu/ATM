"""
# print() #used to print or execute a code
print("Hello World")  # This prints Hello World in the Editor
print("*" * 10)  # This prints * 10 times

# LINTING CODE
print("Hello World")
2 + 3

# FORMATING CODE(pep8 GUIDE STYLE FOR PYTHON CODE)auto formats your code when saved
x = 1
2 = 3
unit_price = 3

students_count = 1000 # variable
print(students_count)

rating = 4.99 #float because of the decimal
is_published = False #Boolean
course_name = "Python Programming" # string


#strings
course = "Python Programming"
print(len(course))#bulit-in functions to check the lenth of a string.that is the number of characters
#functions use (). used to call the function
# if you  want to give access to a particular character in a string you use []
print(course[0])# 0 being the first element in the string -1 is for the lastname element
print(course[-1])
print(course[0:3])#extract first 3 charcters
print(course[0:])#gives you the whole string
print(course[:3])# default put 0 and gives on;y the first 3
print(course[:])
 
  #ESCAPE SEQUENCES (\, #, \",\', \\, \n=new line  )
course = "Python \nProgramming"
print(course)
# \ ESCAPE CHARACHER

#FORMATTED STRINGS
first = "Sarah"
last = "Baidu"
full = f"{len(first)} {last}"
print(full)

#STRING METHODS
course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())# remove wide spaces
print(course.find("gra")) #index of a character
print(course.replace("p", "j"))
print("pro" in course) # checks if we have pro in course 
print("swift" not in course) #checks if its not in course

#NUMBERS
x = 1 #int
x = 1.1 #float
x =1 + 2j # a + bi complex i=imaginary number

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) # gives a float
print(10 // 3) # no decimals
print(10 % 3) # remainder
print(10 ** 3) # exponent/power

x = 10
x = x + 3
x+=3 #increase x by 3

import math

#WORKING WITH NUMBERS
print(round(2.1)) # rounds the number
print(abs(-2.1))#return the absoulte value of a number


# TYPE CONVERSION
x = input("x: ")  # input always come as a string
y = int(x) + 1
print(f"x: {x}, {y}")
"""
# we can't concantenate two different things
# int(x)
# float(x)
# bool(x) =falsey ="", 0, None
# str(x)


 