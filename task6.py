#TASK SIX
#GENERATORS, LIST COMPREHENSION AND DECORATORS


"""

1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.



statement = "Think and Be 'like a Proton' "
res =[]
for ch in statement:
    if ch.isupper():
        res.append(ch)
print(res)




2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}



# using dictionary comprehension
# using two for loops

students= ['Smit','Jaya','Rayyan']
subjects = ['CSE','Networking','Operating System']
res = {}
for key in students:
    for value in subjects:
        res[key] = value
        subjects.remove(value)
        break
print(res)




3. Learn More about Yield, next and Generators


# generators and yield: (yield = to end a function, and returns a generator)
# example: def infinite_sequence():
#              num = 0
#              while True:
#                 yield num
#                 num += 1
# This looks like a typical function definition, except for the Python yield
# statement and the code that follows it. yield indicates where a value is sent back to the caller,
# but unlike return, you don’t exit the function afterward.
#
# yield: Its primary job is to control the flow of a generator function in a way that’s similar to return statements
# When you call special methods on the generator, such as next(), the code within the function is executed up
# to yield.
# When the Python yield statement is hit, the program suspends function execution and returns the yielded value
# to the caller. (In contrast, return stops function execution completely.) When a function is suspended, the state
# of that function is saved. This includes any variable bindings local to the generator, the instruction pointer,
# the internal stack, and any exception handling.
# ref: realpython.com

# next: The next() function returns the next item in an iterator.
# syntax: next(iterable, default)
# we can add a default return value, to return if the iterable has reached to its end.
# iterable = Required. An iterable object.
# default = Optional. An default value to return if the iterable has reached to its end.
# example: to create an iterator, and print the items one by one
# mylist = iter(["apple", "banana", "cherry"])
# x = next(mylist)
# print(x)
# x = next(mylist)
# print(x)
# x = next(mylist)
# print(x)
# ref: w3schools.com



4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for input_string in rev_str("Consultadd Training"):
    print(input_string)




5. Write an example on decorators.

def example_decorator(func):
    def inside_func():
        print("Covid is cruel!")
        func()
        print("It ruined lives!")
    return inside_func

def very_func():
    print("Very cruel!")

very_func = example_decorator(very_func)
very_func()



"""