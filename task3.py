"""
DATA STRUCTURES


1. Create a list of 10 elements of four different data types like int, string, complex and float.

elements = ["word", 2.3, True, (1, 3j), 55, 'O', (9j), 10, 33.33, ['a']]
print(elements)


2. Create a list of size 5 and execute the slicing structure


elements = ["word", 2.3, 55, 10, 63]
print(elements[1:3])



3. Write a program to get the sum and multiply of all the items in a given list.


elements = [1,2,3,4,5]
sum_elements, multiply_elements = 0, 1
for i in elements:
    sum_elements = sum_elements + 1
    multiply_elements *= i
print("The sum of elements = ", sum_elements)
print("The product of elements = ", multiply_elements)




4. Find the largest and smallest number from a given list.



elements = [159,20,120,40,90]
print("The smallest number from the list = ", min(elements))
print("The largest number from the list = ", max(elements))




5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.


new_elements = [2, 4, 7, 10, 69, 101, 38, 70, 99]
result = []

for i in new_elements:
    if i % 2 != 0:
        result.append(i)
print(result)



6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and 30 (both included).



elements = []

for i in range(1, 30):
    if i < 6:
        elements.append(i * i)
    if i > 24:
        elements.append(i * i)

print(elements)



7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]


elements1 = [1,3,5,7,9,10]
elements2 = [2,4,6,8]

elements1.remove(elements1[-1])
new_elements = elements1+ elements2
print(new_elements)



8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}


a={1:10,2:20}
b={3:30,4:40}

print("Values in a and b are: ", a,  b)

a.update(b)
print("Concatenating both dictionaries = ", a)



9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}


n=5
dic={}

for i in range (1,6):
    dic[i] = i*i
print(dic)



10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)



userNumbers = input('Enter sequence of comma-separated numbers: ')

print(userNumbers.split(','))
print(tuple(userNumbers.split(',')))







"""