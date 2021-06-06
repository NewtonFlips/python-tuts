# Data Types

# Integers
# these are numbers without decimal points.
# these should not be in quotes

a = 10
print(a, type(a))


# FLoats
# these are numbers with decimal points.
# these should not be in quotes
b = 10.45
print(b, type(b))

# Strings
# these are piences of words or long sentences or enve paragraphs
# these should be in quotes

c = 'Hello world'
print(c, type(c))

# List (data structure)
# multiple values can be stored of multiple data types
# lists are mutable, like more items can be added
student_grades = [8.5, 7.6, 9.1, 8.1]
print(student_grades, type(student_grades))

my_sum = sum(student_grades)
num_items = len(student_grades)
average = my_sum / num_items
print(average)

# student_grades.count(9.1) - counts all numbers in the list where value is 9.1

# Generate list automatically for numbers
# The last number will not be included
new_list = list(range(1, 10))
print(new_list)


# dictionary (data structure)
# its a data structure with key value pairs

# will give a list type data structure
grades_students = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
total_grades = sum(grades_students.values())
grades_length = len(grades_students)
mean = total_grades / grades_length
print(mean)

# Tuples
# Just like list but with paranthesis
# these are immutables, like new items cannot be added or items cannot be removed from tuples
# they are bit faster than lists
first_tuple = (1, 2, 3)


'''
Cheatsheet (Data Types)

In this section, you learned that:

    Integers are for representing whole numbers:

    rank = 10
    eggs = 12
    people = 3

    Floats represent continuous values:

    temperature = 10.2
    rainfall = 5.98
    elevation = 1031.88

    Strings represent any text:

    message = "Welcome to our online shop!"
    name = "John"
    serial = "R001991981SW"

    Lists represent arrays of values that may change during the course of the program:

    members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
    pixel_values = [252, 251, 251, 253, 250, 248, 247]

    Dictionaries represent pairs of keys and values:

    phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
    volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

    Keys of a dictionary can be extracted with:

    phone_numbers.keys()

    Values of a dictionary can be extracted with:

    phone_numbers.values()

    Tuples represent arrays of values that are not to be changed during the course of the program:

    vowels = ('a', 'e', 'i', 'o', 'u')
    one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    To find out what attributes a type has:

    dir(str)
    dir(list)
    dir(dict)

    To find out what Python builtin functions there are:

    dir(__builtins__)

    Documentation for a Python command can be found with:

    help(str)
    help(str.replace)
    help(dict.values)
    '''
