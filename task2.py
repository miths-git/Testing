"""
1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string.


n = int(input("Enter a number: "))

def divisible(n):
    if (n % 3 == 0) and (n % 5 == 0):
        print("Consultadd - Python Training")
    elif (n % 3 == 0):
        print("Consultadd")
    elif (n % 5 == 0):
        print("Python Training")
    else:
        print("The number is not divisible by 3 nor 5")
divisible(n)




2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action



option = int(input("Choose your option, 1 to 5 : "))


def function(option):
    global num1, num2, num3, num4
    if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
        num1 = int(input("Enter the number :"))
        num2 = int(input("Enter the number :"))
    elif option == 5:
        num3 = int(input("Enter the number :"))
        num4 = int(input("Enter the number :"))
    if option == 1:
        ans = (num1 + num2)
        if ans > 0:
            print(ans)
        else:
            print("Negative")
    elif option == 2:
        ans = (num1 - num2)
        if ans > 0:
            print(ans)
        else:
            print("Negative")
    elif option == 3:
        ans = (num1 / num2)
        if ans > 0:
            print(ans)
        else:
            print("Negative")
    elif option == 4:
        ans = (num1 * num2)
        if ans > 0:
            print(ans)
        else:
            print("Negative")
    elif option == 5:
        ans = (num1 + num2 + num3 + num4 / 4)
        if ans > 0:
            print(ans)
        else:
            print("Negative")

function(option)




3. Write a program to implement the flowchart


a,b,c = 10,20,30

avg = (a + b + c) / 3
print("avg = ", avg)

if (avg > a and avg > b and avg > c):
    print("avg is higher than a, b, c")
elif (avg > a and avg > b):
    print("avg is higher than a, b") # in the flowchart it says avg is higher than a,b, c
elif (avg > a and avg > c):
    print("avg is higher than a, c")
elif (avg > b and avg > c):
    print("avg is higher than b, c")
elif (avg > a):
    print("avg is just higher than a")
else:
    if (avg > b):
        print("avg is just higher than b")
    elif (avg > c):
        print("avg is just higher than c")




4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”


while True:
    user_input = int(input("Enter a number: "))
    if (user_input < 0):
        print("It's Over")
        break
    else:
        print("Good Going")




5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.


result = []
for i in range(2000, 3201):
    if i % 7 == 0:
        if i % 5 != 0:
            result.append(i)
print(result)


    

6. What is the output of the following code examples?

x = 123
for i in x:
  print(i)

# output = TypeError: 'int' object is not iterable
# 1 warning 1 weak warning


i = 0
while i < 5:
  print(i)
  i += 1
  if i == 3:
    break
  else:
    print(“error”)

# Output: SyntaxError: Invalid character in identifier
# 7 errors


count = 0
while True:
  print(count)
  count += 1
  if count >= 5:
    Break

# Output: NameError: name 'Break' is not defined
# 1 error 1 warning 3 weak warnings



7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement


for i in range(0, 6):
    if i == 3 or i == 6:
        continue
    print(i)




8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2

digits , letters = 0 , 0
user_input = str(input("Enter your input: "))

for i in user_input:
    try:
        int(i)
        digits = digits + 1
    except:
        letters += 1

print("The count of digits: ", digits)
print("The count of letters: ", letters)



9. Read the two parts of the question below:

Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)




10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
counter = 1
While counter <= 5:
    print(“Type in the”, counter, “number”
    counter=counter+1

The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.



counter, luckyNumber = 1, 100

while counter <= 5:
    user = eval(input("Enter a number: "))
    counter = counter + 1
    if (user == luckyNumber):
        print("Good guess!")
    elif counter <= 5:
        print("Try again!")
print("Game over!")




11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.


counter, luckyNumber = 1, 100

while counter <= 5:
    user = eval(input("Enter a number: "))
    counter = counter + 1
    if (user == luckyNumber):
        print("Good guess!")
        break
    elif counter <= 5:
        print("Try again!")
    else:
      print("Sorry but that was not very successful")




"""