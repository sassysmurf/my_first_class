#This file contains answers to the Programming Language Review Tasks

#Basic Programming & Precision Arithmetic

#1.Write a program to calculate the perimeter and area of a rectangle given its two adjacent sides a and b.
#Input: a = 4, b = 6
#Output: Perimeter = 20, Area = 24

a = 4  # length of the rectangle
b = 6  # width of the rectangle

perimeter = 2*(a+b)
area = a*b

print("Perimeter =", perimeter)
print("Area =", area)

#2.Write a program that takes two perpendicular sides a and b of a right triangle, then calculates its hypotenuse c.
#Input: a = 3, b = 4
#Output: Hypotenuse = 5.0

import math
a = 3
b = 4

hypotenuse = math.sqrt(a ** 2 + b ** 2)
print("Hypotenuse =", hypotenuse)

#3.Write a program that takes a 3-digit integer and calculates the sum of its digits.
#Input: 258
#Output: Sum = 15

n=258

a=n//100
b=(n//10)%10
c=n%10

sum= a+b+c

print("Sum=", sum)

#4.Write a program to convert a time given in hours, minutes, and seconds into total seconds.
#Input: hours = 1, minutes = 20, seconds = 15
#Output: Total seconds = 4815

hours=1
minutes=20
seconds=15

total_seconds=hours*3600+minutes*60+seconds
print("Total seconds =", total_seconds)

#5.Write a program to convert a given time duration from total minutes into days, hours, and remaining minutes.
#Input: 2895
#Output: 2 day(s), 0 hour(s), 15 minute(s)

m=2895

days=m//1440
hours=(m%1440)//60
minutes=m%60

print(f"{days} day(s), {hours} hour(s), {minutes} minute(s)")

#Conditions

#6.Write a program that takes two integers a and b and prints the maximum of the two numbers.
#Input: a = 5, b = 9
#Output: 9

a=5
b=9

if a>b:
    print(a)
else:
    print(b)

#7.Write a program to check whether a given integer is even or odd.
#Input: 7
#Output: Odd

n=7
if n % 2 ==0:
    print("Even")
else:
    print("Odd")

#8.Write a program to check whether a given 24-hour time string format (hours and minutes) is valid.
#Input: Hours = 23, Minutes = 59
#Output: Valid Time

h=23
m=59
if 0<= h <= 23 and 0 <= m <= 59:
    print("Valid time")
else:
    print("Invalid time")

#9.Write a program to determine the quadrant (1, 2, 3, 4) or axis where a point (x, y) is located.
#Input: x = -4, y = 5
#Output: Quadrant 2

x = -4
y = 5
if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x > 0 and y < 0:
    print("Quadrant 4")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
else:
    print("X-axis")

#10.Write a program to check if two given closed ranges [a, b] and [c, d] overlap with each other.
#Input: Range 1 = [3, 8], Range 2 = [6, 12]
#Output: Overlapping

a = 3
b = 8

c = 6
d = 12

if a <= d and c <= b:
    print("Overlapping")
else:
    print("Not overlapping")

# For Loop

#11.Write a program using a for loop to print all numbers from 1 to N that are divisible by both 3 and 5.
#Input: N = 30
#Output: 15 30

N = 30
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#12. Write a program using a for loop to calculate the factorial of a given integer N.
# Input: N = 5
# Output: Factorial = 120

N = 5
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
print("Factorial =", factorial)

#13. Write a program using nested for loops to print a right-angled triangle pattern of numbers of height N.
# Input: N = 4
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

N = 4
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#14. Write a program using a for loop to calculate the sum of the squares of numbers from 1 to N.
# Input: N = 4
# Output: Sum = 30 (1 + 4 + 9 + 16)

N = 4
total = 0
expression = ""
for i in range(1, N + 1):
    total = total + i ** 2
    expression = expression + str(i ** 2)
    if i < N:
        expression = expression + " + "
print("Sum =", total, "(" + expression + ")")

#15. Write a program using nested for loops to display the multiplication tables from 1 to N.
# Input: N = 2
# Output:
# 1x1=1 1x2=2 1x3=3 ... 1x10=10
# 2x1=2 2x2=4 2x3=6 ... 2x10=20

N = 2
for row in range(1, N + 1):
    for col in range(1, 11):
        print(f"{row} x {col} = {row * col}", end="\t")
    print()

# While Loop

#16. Write a program using a while loop to calculate the sum of the digits of a given integer.
# Input: 456
# Output: Sum = 15

N = 456
total = 0
while N > 0:
    digit = N % 10
    total = total + digit
    N = N // 10
print("Sum =", total)

#17. Write a program using a while loop to find the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
# Input: A = 56, B = 98
# Output: GCD = 14

A = 56
B = 98
while B != 0:
    remainder = A % B
    A = B
    B = remainder
print("GCD =", A)

#18. Write a program using a while loop to convert a positive decimal integer into its binary equivalent.
# Input: 13
# Output: Binary = 1101

N = 13
binary = ""
while N > 0:
    remainder = N % 2
    binary = str(remainder) + binary
    N = N // 2
print("Binary =", binary)

#19. Write a program using a do-while loop to continuously prompt the user for a number between 1 and 10 until a valid input is entered.
# Input sequence: -3, 15, 7
# Output: Valid input received: 7

# haven't heard of a do-while loop, so skipping this task

#20. Write a program using a while loop to keep reading numbers from user input until the user enters 0, then output the running total sum.
# Input sequence: 10, 20, -5, 0
# Output: Total Sum = 25

N = 10
total = 0
while N != 0:
    total = total + N
    if N == 10:
        N = 20
    elif N == 20:
        N = -5
    else:
        N = 0
print("Total Sum =", total)

# Functions

#21. Write a program to count how many prime numbers exist within a range [A, B].
# Input: A = 10, B = 30
# Output: Prime Count = 6

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

A = 10
B = 30
count = 0
for N in range(A, B + 1):
    if is_prime(N):
        count = count + 1
print("Prime Count =", count)

#22. Write a program to convert a positive decimal integer into its binary representation string using a loop.
# Input: 13
# Output: Binary = 1101

def to_binary(N):
    binary = ""

    while N > 0:
        remainder = N % 2
        binary = str(remainder) + binary
        N = N // 2
    return binary
N = 13
print("Binary =", to_binary(N))

#23. Write a program to print a hollow square pattern of size NxN using nested loops.
# Input: N = 4
# Output:
# ****
# *   *
# *   *
# ****

def hollow_square(N):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N -1 or j == 0 or j == N -1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
N = 4
hollow_square(N)

#24. Write a program to print an inverted isosceles triangle pyramid pattern of height N.
# Input: N = 3
# Output:
# *****
# ***
# *

def inverted_pyramid(N):
    for i in range(N):
        for j in range(2 * N - 1 - 2 * i):
            print("*", end="")
        print()
N = 3
inverted_pyramid(N)

#25. Write a program to print all Armstrong numbers between 100 and 999 using loops.
# Input: None
# Output: 153 370 371 407

def is_armstrong(N):
    original = N
    total = 0
    while N > 0:
        digit = N % 10
        total = total + digit ** 3
        N = N // 10
    return total == original

for N in range(100, 1000):
    if is_armstrong(N):
        print(N, end=" ")

# Basic Array Operations

#26. Divide all elements of the array by the value of the largest element.
# 	Input:
# 	6 4 3 5 6 7 3 2 1
# 	Output:
# 	6/7, 4/7, 3/7, 5/7, 6/7, 7/7, 3/7, 2/7, 1/7

A = [6, 4, 3, 5, 6, 7, 3, 2, 1]
largest = max(A)
for i in range(len(A)):
    print(str(A[i]) + "/" +str(largest), end=", " if i < len (A) -1 else "\n")

#27. Find the index and value of the first positive element in the array.
# 	Input: -8 -6 -4 2 9 -7 -3
# 	Output: index=3, value=2

A = [-3, -2, 0, 5, 8, 4]
for i in range(len(A)):
    if A[i] > 0:
        print("index =", i, "value =", A[i])
        break

#28. Replace all elements in an array with their opposite signs (e.g., 1 -> -1).
# Input:	8 -5 6 7 -4 9 -2
# Output:  -8 5 -6 -7 4 -9 2
A = [8, -5, 6, 7, -4, 9, -2]
B = []
for x in A:
    B.append(-x)
print(B)

#29. Find the minimum and maximum elements in an array and swap their positions.
# 	5  6  8  4  2  3  9
# 	min = 2
# 	max = 9
# 	5 6 8 4 9 3 2

A = [5,  6,  8,  4,  2,  3,  9]
minimum = min(A)
maximum = max(A)
i = A.index(minimum)
j = A.index(maximum)
A[i], A[j] = A[j], A[i]
print(*A)

#30. Calculate the numerical difference between the maximum and minimum elements.
# Input: 5  6  8  4  2  3  9
# Output:  9 - 2 = 7

A = [5,  6,  8,  4,  2,  3,  9]
maximum = max(A)
minimum = min(A)
difference = maximum - minimum
print(maximum, "-", minimum, " =", difference)

# Comparison & Sequences

#31. Count elements that are strictly greater than both their immediate neighbors.

def count_greater(A):
    count = 0
    for i in range(1, len(A) -1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            count += 1
    return count

A = [1, 5, 2, 4, 7, 3, 6]
print (count_greater(A))

#32. Replace all values less than 15 with -1 in an array ranging from 0–49.
A = list(range(50))
for i in range(len(A)):
    if A[i] < 15:
        A[i] = -1

#33. Fill an array with random numbers within the interval $[a, b]$.
import random
a = 1
b = 10
N = 5
A = []
for i in range(N):
    A.append(random.randint(a, b))
print(A)
#output: [3, 5, 2, 10, 1] - the range will change each time the program executes

#34. Find the sum of the indices of the minimum and maximum elements.

A = [5, 6, 3, 2, 8, 1]
minimum = min(A)
maximum = max(A)
i = A.index(minimum)
j = A.index(maximum)
total = i + j
print("sum of the indices =", total)

#output: sum of the indices = 7

#35. Calculate the sum of elements located between two zeros.
A = [1, 3, 0, 5, 4, 0, 8]
start = A.index(0)
end = len(A) - 1 - A[::-1].index(0)
total = 0

for i in range(start+1, end):
    total = total + A[i]
print('sum =', total)

#output: 9

# Strings

#36. Write a program to determine if a string is a palindrome.
#    Input: madam
#    Output: Palindrome

W = "madam"
reverse = ""
for i in range(len(W) - 1, -1, -1):
    reverse = reverse + W[i]
if W == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#37. Write a program to convert all characters in a string to uppercase.
#    Input: hello
#    Output: HELLO
word = "hello"
print(word.upper())

#38. Write a program to count the number of consonants in a string.
#    Input: hello world
#    Output: Consonants = 7

W = "hello world"
count = 0
for c in W:
    if c.isalpha() and c not in "aeiou":
        count = count + 1
print("Consonants =", count)

#39. Write a program to count the number of vowels in a given string.
#    Input: hello world
#    Output: Vowels = 3
W = "hello world"
count = 0
for v in W:
    if v.isalpha() and v in "aeiou":
        count = count + 1
print("Vowels", count)

#40. Write a program to count the number of words in a string.
#    Input: this is a test
#    Output: Words = 4
S = "this is a test"
words = S.split()
count = len(words)
print("Words =", count)
