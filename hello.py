# Hello world
msg = "Hello World"
print(msg)

# Hello (name)
name = "Mike"
print("Hello", name)

# Python indentation specificity == 4 spaces 
x = 1
if x == 1:
    # indented 4 spaces
    print("x is 1.")

# int
myint = 7
print(myint)

# float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# simple operators on numbers and strings
one = 1
two = 2
three = one + two
print(three)

# string concatenation
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assign more than one variable "simultaneously"
a, b = 3, 4
print(a)
print(a, b)

# mixing operators between numbers and strings not supported
one = 1
two = 2
hello = "hello"
#print(one + two + hello)

# LISTS - very similar to arrays - contain any type of variable - can be iterated
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1

# prints 1,2,3
for x in mylist:
    print(x)

# accessing indices that don't exist == exception
mylist = [1, 2, 3]
# print(mylist[10])

# Arithmetic
number = 1 + 2 * 3 / 4.0
print(number)

# modulo / remainder
remainder = 11 % 3
print(remainder)

# power relationships
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# strings can multiply
lotsofhellos = "hello" * 10
print(lotsofhellos)

# joining lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# new list with repeating sequence using multiply
print([1, 2, 3] * 3)

x = object()
y = object()

# Challenge Example
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# STRING FORMATTING

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# Two or more argument specifiers
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# Any object which is not a string can also use the %s operator  - "repr" method?
# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# This prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# This prints out 4, because the location of the first occurrence of the
# letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase -
# this method only recognizes the first.

astring = "Hello world!"
print(astring.index("o"))

# Count the number of l's in the string:
astring = "Hello world!"
print(astring.count("l"))

# This prints a slice of the string, starting at index 3, and ending at index 6.

astring = "Hello world!"
print(astring[3:7])

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

# There is no function like strrev in C to reverse a string.
# But with the above mentioned type of slice syntax you can reverse a string

astring = "Hello world!"
print(astring[::-1])

# Case changes in str

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something
# or ends with something, respectively.

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list.

astring = "Hello world!"
afewwords = astring.split(" ")

# Python uses boolean logic to evaluate conditions.

x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# The "and" and "or" boolean operators allow building complex boolean expressions

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator could be used to check if a specified object exists
# within an iterable object container

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other
# space size will work, as long as it is consistent.
# Notice that code blocks do not need any termination.

# Here is an example for using Python's "if" statement using code blocks:

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# A statement is evaluated as true if one of the following is correct:
# 1. The "True" boolean variable is given, or calculated using an expression,
# such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.

# Here are some examples for objects which are considered as empty:
# 1. An empty string: ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

# Unlike the double equals operator "==", the "is" operator
# does not match the values of the variables, but the instances themselves.
# For example:

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# not operator inverts a boolean expression

print(not False)  # Prints out True
print((not False) == (False))  # Prints out False

# For loops iterate over a given sequence. Here is an example:

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# For loops can iterate over a sequence of numbers using
# the "range" and "xrange" functions.

# range returns a new list with numbers of specified range
# xrange returns iterator (more efficient)
# Python 3 uses the range function which acts like xrange

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# While loops repeat as long as a certain boolean condition is met.

# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# break is used to exit a for loop or a while loop,
# whereas continue is used to skip the current block,
# and return to the "for" or "while" statement.

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Unlike languages like C,C++.. we can use else for loops.
# When the loop condition of "for" or "while" statement fails
# then code part in "else" is executed.
# If a break statement is executed inside the for loop
# then the "else" part is skipped.
# Note that the "else" part is executed even if there is a continue statement.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# FUNCTIONS

# Functions in python are defined using the block keyword "def", 
# followed with the function's name as the block's name. For example:

def my_function():
    print("Hello From My Function!")
    
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    
def sum_two_numbers(a, b):
    return a + b
  
# CLASSES AND OBJECTS

# Objects are an encapsulation of variables and functions into a single entity. 
# Objects get their variables and functions from classes. 
# Classes are essentially a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# to assign the above class(template) to an object you would do the following:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# To access the variable inside of the newly created object "myobjectx" 
# you would do the following:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable

# So for instance the below would output the string "blah":

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)

# You can create multiple different objects that are of the same class
# (have the same variables and functions defined). 
# However, each object contains independent copies of the variables defined in the class. 
# For instance, if we were to define another object with the "MyClass" class 
# and then change the string in the variable above:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# To access a function inside of an object you use notation 
# similar to accessing a variable:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()

# A dictionary is a data type similar to arrays, 
# but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, 
# which is any type of object (a string, a number, a list, etc.) 
# instead of using its index to address it.

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# or

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# Dictionaries can be iterated over, just like a list. 
# However, a dictionary, unlike a list, does not keep the order 
# of the values stored in it. 
# To iterate over key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
# To remove a specified index, use either one of the following notations:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

# or

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

# MODULES

# https://www.learnpython.org/en/Modules_and_Packages