"""
1) Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
E.g. :
a = 1,
b = 2.01,
c = 'string'

x = 1
y = 2.01
z = 'string'
print(x,y,z)
type(x)
type(y)
type(z)


2) Create a variable of type complex and swap it with another variable of type integer

a = 1 + 1j
print(type(a))
b = 1
print(type(b))
X = a
a = b
b = X

print('The values of a and b are: \n', a, b)


3. Swap two numbers using a third variable and do the same task without using any third variable

a , b = 2 , 5
print("The values of a and b are: \n", a , b)
X = a
a = b
b = X
print("The swapped values of a and b are: \n", a , b)

p , q = 10 , 20
print("Values of p and q before swapping: \n", p , q)
p , q = q , p
print("Without third variable swapping of p and q, p = \n ", p)
print("Without third variable swapping of p and q, q = \n ", q)


4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.


# python version 2.x
data = raw_input("Enter your data: ")
type(data)

# python version 3.x
input_data = eval(input("Enter your data: "))


5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.


print("Enter any two numbers between 1 to 10:")
m = int(input("m: "))
n = int(input("n: "))
z = m + n
print("value is z now is: ", z)
z += 30
result = z
print("The final result is: ", result)



6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc


Data = eval(input("Enter your data: "))
print("The data type of the input value is : ", type(Data))



7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.


# Upper CamelCase
x = "InputData"
print(x)

# Lower CamelCase
y = "inputData"
print(y)

# SnakeCase
z = "input_data"
print(z)

# Uppercase
w = "full_name"
print("full_name.upper()")


8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?


# Example
a = 10
print(a)

a = 100
print(a)

# The Value of 'a' first assigned is 10 and then changes to 100, it will take the latest value assigned.
# The variable values are mutable

"""