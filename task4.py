"""
TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
HIGHER ORDER FUNCTIONS


1. Write a program to reverse a string.
Sample input: “1234abcd”
Expected output: “dcba4321”



def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str

s = "Today is a wonderful day!"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))




2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12



def upper_lower(s):
    up_case = sum(1 for i in s if i.isupper())
    low_case = sum(1 for i in s if i.islower())
    print( "Number of uppercase characters : %s\nNumber of lower case characters : %s" % (up_case,low_case))

upper_lower("asdWDJKKsasf")





3.Create a function that takes a list and returns a new list with unique elements of the first list.


def unique(list):
  x = []
  for s in list:
    if s not in x:
      x.append(s)
  return x

print(unique([1,2,2,2,2,4,9,6,7,8,3,3,3,3,4,5]))




4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.


print("Enter a hyphen separated sequence of words:\n")
l=[n for n in input().split('-')]
l.sort()
print("After sorting alphabetically:")
print('-'.join(l))




5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT



lines = []
print("Sequence of lines: ")

while True:
	line = input("> ")
	if not line:
	    break
	lines.append(line.upper())

print(lines)




6. Define a function that can receive two integral numbers in string form and compute their sum and print it in
the console.


def numbers(s1,s2):
	print(int(s1) + int(s2))
print("The sum of the numbers:")
numbers("10","20")



7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.


def two_numbers(l1,l2):
	len1 = len(l1)
	len2 = len(l2)
	if len1 > len2:
		print(l1)
	elif len2 > len1:
		print(l2)
	else:
		print(l1)
		print(l2)

two_numbers("one","one")




8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).



def values():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(tuple(l))

values()



9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD


def showNumbers(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            print(i,'EVEN')
        else:
            print(i,'ODD')
showNumbers(4)



10.Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)


def even_numbers(x):
    return x%2==0
even = filter(even_numbers,range(1,21))
print(list(even))




11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.



def even_numbers(x):
    return x % 2 == 0

def squares(x):
    return x * x

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = map(squares , filter(even_numbers, l))
print(list(l))




12. Write a function to compute 5/0 and use try/except to catch the exceptions



def value():
    return 5/0
try:
    value()
except ZeroDivisionError as ze:
    print("Any integer number divided by digit zero is a ZERO!")
except:
    print("Any other exception")





13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

import functools
import operator

original_list = [1,2,3,4,5,6,7] #List to be flattened
flatten_list = functools.reduce(operator.iconcat, original_list,[])

print("Original List:", original_list)
print("Flattened List:", flatten_list)



15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.




16. What is the output of the following codes:
(i)

def foo():
try:
   return 1
finally:
   return 2
k = foo()
print(k)


(ii)

def a():
try:
    f(x, 4)
finally:
    print('after f')
    print('after f?')
a()



"""