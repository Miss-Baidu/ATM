"""
# COMPARISON OPERATORS
# =, ==, >, <, ETC

# CONDITIONAL STATEMENTS (IF STATEMENT)
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature < 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

#TENARY OPERATOR

age = 22
if age >= 18:
    message = ("Eligible")
else:
    message = ("Not eligible")

    similar way
age = 17
message = "Eligible" if age >= 18 else "Not Eligible" tenary operator
print(message)

#logial operators(and or not)
high_income = False
good_credit = True
student = False
#if not student:
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

#logical operators are short circuit
#SHORT CIRCUIT EVALUATIONS ( with and operator Continues when all confitions are true. if one is false it doesnt work and would false even if others meet the conditions)
high_income = False
good_credit = True
student = True

if high_income or good_credit or not student:
    print("Eligible")


#CHAINING COMPARISON OPERATORS

# age should be between 18 and 65
age = 22
#if age >= 18 and age< 65:
if 18<= age < 65:
    print("Eligible")

#FOR LOOPS(to create repeatition)
for number in range(1, 10, 3):
    print("Attempt", number, number  * ".")

#for else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
      print("Attemped 3 times and failed")


#NESTED LOOP(PUTTING LOOPS IN LOOPS)inner loop first then outer loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#ITERATIONS
for x in range(5):
    print(x)


print(type(5))
print(type(range(5)))

#iterable
for x in [1,2,3,4]:
    print(x)
shoppig_cart = ["Apple", "Banana", "Cat", "Dog"]
for item in shoppig_cart :
    print(item)


#while loops code runs till you type quit
number = 100
while number > 0:
    print(number)
    number = number // 2

command =""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

#infinte loop
while True: 
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break


    #EXECRISE
for number in range(1, 10):
    if number % 2 ==  1:
        print(number)
print ("We have 4 even numbers")


#functions
#ptint()
#round()

def greet():
    print("Welcome abord")

greet ()

#ARGUMENTS an argument is a value that you pass to a function or method when you call it.
def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome abord")

greet ("Sarah", "Baidu")
greet ("John", "Davis")

#TYPES OF FUNCTIONS
def greet(name):
    print(f"Hi {name}")
#1 PERFORM TASKS
#2 RETURN A VALUE

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Sarah")
file = open("context.txt", "w")
file.write(message)

def greet(name):
    return f"Hi {name}"

print(greet("Sarah"))

#keyword arguments
def increment(number, by):
    return number + by
print(increment (2, by=1))
#print(result)

#default arguments
def increment(number, by=1, ):
    return number + by
print(increment (2, 5))


#args, what
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total *number
        return total
        #total *= number

multiply(2, 3, 4, 5)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Soccer"]
acts = ["Soccer", "Baseball", "Tennis"]
#for x in days:
#for y in act:
    #print (x, y)
for day in days:
  for act in acts:
     if day == act:
        print("Found")

     else:
        print("Not found")

  """  
for x in range(1, 10):
   print(x)
     
 