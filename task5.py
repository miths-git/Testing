
#TASK FIVE
#FILE HANDLING AND EXCEPTION HANDLING


"""

1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError


def eh(a,b):
    try:
        if a == b:
            print("Print this message if a and b are equal!")
        raise SyntaxError
    except SyntaxError:
        print("There is a Syntax error")

eh(1,10)



2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.


import os,sys
try:
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("Entered name is incorrect. Please enter the correct file again.")

# I am not sure on this one

"""

"""

3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”

try:
    nums = input("Enter a four digit number: ")
    if len(nums) == 4:
        print("The four digit number is ", nums)
    else:
        raise OverflowError

except OverflowError:
    print("The length is too short/long !!! Please provide only four digits")

"""


"""
4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.


try:
    UserName = input("Please enter your username: ")
    PassWord = input("Please enter your password: ")
    ReEnter = input("Please enter your password again: ")
    count = 1
    while count < 3:
        if PassWord != ReEnter:
            print("The passwords do not match, please try again: ", count)
            PassWord = input("Enter your password once again: ")
            count = count + 1

        else:
            print(" You are successfully logged in")
            break

    if count == 4:
        print("Your account is temporarily locked, try again after 30 minutes.")

except:
    print(" Syntax error")






5. Go through the link provided below to understand finally and raise concept:
https://www.programiz.com/python-programming/exception-handling


# went through the link and saw the video on different kinds of exception handling



6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.

"""
