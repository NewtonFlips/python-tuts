# syntax for functions
'''
def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean


print(mean([1, 4, 4]))
'''
# if function does not return anything, the function returns none which is a special data type.


# Conditionals

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(mean({"a": 1, "b": 4, "c": 4}))


'''
Bonus Code: Using "and" and "or" in a Conditional

You learned to check for one single condition:

    x = 1
     
    if x == 1:
        print("Yes")
    else:
        print("No")

You can also check if two conditions are met at the same time using an and operator:

    x = 1
    y = 1
     
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")

That will return Yes since x == 1 and y ==1 are both True.

You can also check if one of two conditions are met using an or operator:

    x = 1
    y = 1
     
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")

That will return Yes since at least one of the conditions is True. In this case x == 1 is True.
'''

'''
Cheatsheet (Functions and Conditionals)

In this section, you learned to:

    Define a function:

    def cube_volume(a):
        return a * a * a

    Write a conditional block:

    message = "hello there"
     
    if "hello" in message:
        print("hi")
    else:
        print("I don't understand")

    Write a conditional block of multiple conditions:

    message = "hello there"
     
    if "hello" in message:
        print("hi")
    elif "hi" in message:
        print("hi")
    elif "hey" in message:
        print("hi")
    else:
        print("I don't understand")

    Use the and operator to check if both conditions are True at the same time:

    x = 1
    y = 1
     
    if x == 1 and y==1:
        print("Yes")
    else:
        print("No")

Output is Yes since both x and y are 1.

    Use the or operator to check if at least one condition is True:

    x = 1
    y = 2
     
    if x == 1 or y==2:
        print("Yes")
    else:
        print("No")

Output is Yes since x is 1.

    Check if a value is of a particular type with:

    isinstance("abc", str)
    isinstance([1, 2, 3], list)

or

    type("abc") == str
    type([1, 2, 3]) == lst
    '''
