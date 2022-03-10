# 6.
Loops

Introduction to Python

return STEM;

Version 1

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

![](loops%5Cloops0.png)

# The Need for Loops

* When you are writing programs, often you will want to perform the same action many times.
* This can be done with loops and will result in having to write less code
* For example, consider the following prompt: _Write a program to print all nonnegative integers lower than a number chosen by the user using input()._
* This problem involves using the print() statement several times
  * __The amount of times would __  __change __  __based on user input__
* One method of doing this is the  _while loop_ .

# Structure of loops

* A loop contains a  __header __ and a  __body__
  * The  __header__  dictates how the loop behaves (how to loop)
  * The  __body __ is indented (just like an if statement) and contains the code that is to be executed each time the loop "loops"
    * A single "loop" of a loop is called an  __iteration __ or  __cycle__

while (condition):

print("Loop body")

print("I am inside loop")print("Outside loop")

for item in iterable:

print("Loop body")

print("I am inside loop")

print("Outside loop")

# The While Loop

The basic syntax of the while loop is:

while (condition):	do this

...	execute more statements

* First, the loop checks whether the condition after the while keyword is True.
  * __If __ it is True, it executes all statements inside the body of the loop.
* Then, it goes back to the header, checks if the condition is True, and executes the body if it is
* This cycle repeats until the condition becomes False
  * When it is, it will skip the body and continue executing the rest of the program
* You can think about while loops like this: _Execute all the statements in the body _  _while_  _ the _  _condition is_  _ true._

Checks if the condition is true by making sure a < 10

Modifies the variable used in the condition to get closer to the condition

Prints b, this part of the loop will usually be whatever the loop is trying to accomplish(such as a mathematical operation or modifying a string

while a < 10:	print(b)

a += c

# How to Stop while Loops

While Loops need to be stopped to prevent an infinite loop

An infinite loop is a while loop in which the given condition is never false, such as:

The variable for the condition is never being changed, and the condition will be true forever.

Infinite loops resulting in the contents of the while loop repeating until the program crashes or is stopped.

i = 0

while i == 0:

print(“This is an Infinite Loop”)

This program will output “this is an Infinite Loop”) until it is stopped or it crashes

# How to Interact with while Loops

There are other ways to stop or change while loops without changing the condition, the break statement and the continue statement.

The break statement stops the while loop when the code reaches it, even if the condition is met.

i = 1

while i > 0:

print("This is an Infinite Loop")

if i == 5:

break

i += 1

This program will output “This is an Infinite Loop”) 5 times and then stop.

The continue statement will stop the current iteration(repetition) of the while loop and move on to the next one.

i = 0

while i < 10:

i += 1

if i == 5:

continue

print(i)

This program will output the numbers from 1 to 10 but skip 5.

# Ending while Loops

The else statement can be used at the end of while loops to output something else when the condition is no longer true.

__The __  __else __  __clause will only run if the loop doesn't __  __break __  __prematurely__

i = 0

while i < 10:

i += 1

print(i)

else:

print(“The numbers 1-10 have been printed”)

This program will output the numbers 1-10 and then print “The numbers 1-10 have been printed”

# while Loop: Example

Here’s an example of a while loop, solving the problem presented earlier:

x = int(input("Enter a positive number: "))while (x > 0):    x -= 1

print(x)

First, the loop takes the user’s input using input().

Afterwards, it executes the while loop:First, the loop checks if x is greater than zero. If it is, it subtracts 1 from x, and prints it. Then, it repeats this process. When x is zero, the loop ends. Since there are no more lines in the program, the program is finished.

# while Loop Practice

* What is a common way to create an infinite loop?
* When does a while loop check the condition?
  * Once, when the loop is started
  * Twice, at the start and end of the loop
  * Infinite times until the condition is not met or the loop is broken
  * Never, it is there just for show

* What is a common way to create an infinite loop?
* When does a while loop check the condition?
  * Once, when the loop is started
  * Twice, at the start and end of the loop
  * Infinite times until the condition is not met or the loop is broken
  * Never, it is there just for show

# Approaching Loops and Algorithms with Loops

When you’re debugging a very straightforward program like this:

a = input()

b = input() print(a / b)

It’s quite intuitive - you can simply look at each line of the code and see whether it works or not.

However, for loops, this is not the case sometimes.

Many times, when beginners write programs, their problems lie within loops, because they do not follow through each loop.

When going through a loop, remember that the loop only checks for the condition  _at the start of an iteration_

Sometimes your loop may not run at all because the initial condition is not satisfied when the program reaches the loop code

| Iteration | Statement | Value | Explanation |
| :-: | :-: | :-: | :-: |
| 1 | i += 1 | i = 5, j = 0 | Since j < 3 is True, Python enters the loop. |
| 1 | j += 1 | i = 5, j = 1 |  |
| 2 | i += 1 | i = 6, j = 1 | j < 3 is still True, so Python repeats the code. |
| 2  | j += 1 | i = 6, j = 2 |  |
| 3 | i += 1 | i = 7, j = 2 | j < 3 is still True, so Python repeats the code again. |
| 3 | j += 1 | i = 7, j = 3 |  |
| END | N/A | i = 7, j = 3 | j < 3 is now False, so Python stops the loop. |

Analyze this looping code:

i = 4

j = 0

while (j < 3):    i += 1

j += 1

print(i + j)

# The for Loop

* The while Loop executes the content inside the loop while certain conditions are met.
* The for Loop iterates (walks) through a list, string, dictionary, or other data structure
  * If something is able to be iterated (walked through a piece at a time) through, it is classified as  __iterable__
* The basic syntax is:
* The for loop goes across each element of the sequence, after executing the body of the loop every time it moves on to a new element.
* First, we will cover for loops across a range of numbers.

Example of an iterable:

for element in iterable:    execute body of the code

# The for Loop over a range of numbers

To iterate through a set of numbers, you can use the range() function.

The basic format is:

For example:

goes through 0, 2, 4, 6, 8.

If you only give one number, it will use that number as the END and use start = 0 and increment = 1.

If you only give two, it will use the first as START and the second as END and increment will = 1.

__Start:__  Starting value, inclusive

__End: __ Ending value, exclusive

__Increment:__  How much to increase by

for i in range(start, end, increment):    body_of_loop

for i in range(0, 10, 2):    body_of_loop

# Approaching Loops and Algorithms with Loops

Given the loop to the left, let’s see what python does when going through it

for i in range(0, 6):    print(i)

| i = | Statement | Explanation |
| :-: | :-: | :-: |
| 0 | print(i) | First, Python starts the loop with i = 0. It then executes print(i). Since there is no more in the body, the loop then goes to the next value of i. |
| 1 | print(i) | i = 1,so it does print(i), and goes to the next value. |
| 2 | print(i) | i = 2, so it does print(i), and goes to the next value. |
| 3 | print(i) | i = 3, so it does print(i), and goes to the next value. |
| 4 | print(i) | i = 4, so it does print(i), and goes to the next value. |
| 5 | print(i) | i = 5, so it does print(i), and there are no more values. |
| END | N/A | Since there are no more values, the loop ends. |

# The for Loop over a range of numbers(Examples)

for i in range(0, 10, 2):    #body_of_loop

# Iterates through 0, 2, 4, 6, 8

for i in range(0, 10):    #body_of_loop # Iterates through 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(10):    #body_of_loop # Iterates through 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(5, 0, -1):    #body_of_loop # Iterates through 5,4,3,2,1

# The for Loop Over a String

In the previous lessons, you learned that you can access the characters of a string by using str_name[index]. Remember that indices start from 0.

For example:

s = "Hello World"

s[0]

>>> H

s[1]

>>> e

s[5]

>>>

s[6]

>>> W

To iterate through a string, you can create a loop which iterates through a set of numbers, then use those numbers to reference each character:

Remember that you can use len(s) to get the length of the string s.

s = "Hello World"

for i in range(len(s)):     print(s[i])

This code will output “Hello World” with each character on its own line.

While it is possible to use range(), Python has a built in method to iterate over a string:

s = "Hello World"

for i in s:     print(i)

* In this example, i will take on each character of the string s each time the body of the loop is executed.

s = "Hello World"

for i in range(len(s)):     print(s[i])

This method does the same thing as the method presented in the last slide, but is simpler and easier to read.

# break in for loops

If you want a for loop to prematurely end, you can use the keyword break.

s = 'Python' for letter in s:     if letter == 'h':         break

print("Current letter", letter)

>>>	Current letter: P

>>>	Current letter: y

>>>	Current letter: t

In this code, the code iterates through the letters of the string s until reaching ‘h’.

When the code reaches ‘h’ the loop is broken and the code stops.

# continue in for loops

For loops can also use the continue keyword and in for loops this keyword can skip over a current iteration.

s = 'Python' for letter in s:     if letter == 'h':         continue

print("Current letter", letter)

>>>	Current letter: P

>>>	Current letter: y

>>>	Current letter: t

>>>	Current letter: o

>>>	Current letter: n

In this example, the for loops iterates through each letter in the string s but skips h as the if statement followed by the continue keyword skips that iteration of the string.

# else in for loops

The else keyword can be used in for loops to print something when the loop is done,  __if the loop does not exit prematurely with __  __break__

This can be used to output a final remark once the loop is done without incorporating an if statement in your loop.

These two blocks of code output the same thing, but the use of the else statement looks better and is more efficient.

for i in range(10):

print(i)

else:

print(10)

This code prints the letters 0 through 9 with the for loop and then prints 10 with the else statement.

for i in range(10):

print(i)

else:

print(“Those were the numbers 0-9”)

for i in range(10):

print(i)

if i == 9:

print(“Those were the numbers 0-9)

# for Loop Practice

* Which use of the range function goes through every odd number from 1-20?
* Which data type can a for loop not iterate through?
  * Strings
  * Lists
  * Integers

for i in range(20, 2)

for i in range(1,20,2)

for i in range(1,20,1)

for i in range(20,1)

* Which use of the range function goes through every odd number from 1-20?
* Which data type can a for loop not iterate through?
  * Strings
  * Lists
  * Integers

for i in range(20, 2)

for i in range(1,20,2)

for i in range(1,20,1)

for i in range(20,1)

# while loop vs for loop

* Number of iterations
  * In a while loop the number of iterations is unknown
  * In a for loop the number of iterations should be already known
* What a while loop is better at
  * Asking for user input
  * When the increment isn’t increasing by a standard amount each time
* What a for loop is better at
  * Iterating through a list, string, etc.
  * Iterating through a sequence of numbers

# if statement inside of while/for loops

In previous examples, you'll see that we included if statements inside of loops.

if statements simply check for the condition, every time to loop runs

You still need to indent specifically for the if statement.

s = 'Python'for letter in s:    if letter == 'h':        break

print("Current letter", letter)

>>> Current letter: P

>>> Current letter: y

>>> Current letter: t

You can use if statements to check for certain conditions and end loops early, or do operations on specific characters (the character is equal to "a", etc.)

# Nested loops

You can also have loops inside of loops to repeat complex tasks multiple times.

The inner loop would be fully executed every time the outer loop cycles (iterates) one time.

days_of_week = 'MTWTF'for weeks_of_month in range(1,5):

print("week " + str(weeks_of_month))

for day in days_of_week:

print(day)

>>> week 1 # Outer Loop iterates once

>>> M # Inner Loop iteration 1

>>> T # Inner Loop iteration 2

>>> W # Inner Loop iteration 3

>>> T # Inner Loop iteration 4

>>> F # Inner Loop iteration 5

>>> week 2 # Outer loop iterates once

>>> M # Inner Loop iteration 1

>>> T # Inner Loop iteration 2

>>> W # Inner Loop iteration 3

>>> T # Inner Loop iteration 4

>>> F # Inner Loop iteration 5

>>> week 3 # Outer loop iterates once

>>> M # Inner Loop iteration 1

>>> T # Inner Loop iteration 2

>>> W # Inner Loop iteration 3

>>> T # Inner Loop iteration 4

>>> F # Inner Loop iteration 5

>>> week 4 # Outer loop iterates once

>>> M # Inner Loop iteration 1

>>> T # Inner Loop iteration 2

>>> W # Inner Loop iteration 3

>>> T # Inner Loop iteration 4

>>> F # Inner Loop iteration 5

# Defensive Programming

* Any program you write that requires user input should be  __defensive__
  * They should be able to deal with any input the user enters, even if it is invalid
    * The program should not crash whenever the user enters invalid input
* This can be done using if __ __ statements to check user input and while loops to restart the program

while True:

x = input("Please enter a three letter word")

if len(x) == 3:

break

print("The word you entered is not three letters long. Please try again")

# Do something with the three letter word

# We now know for sure it is three letters and a string

You can and should perform any check that may crash the program:

print("This program does division for you")

while True:

x = input("Enter a positive integer dividend: ")

y = input("Enter a positive integer divisor: ")

if not (x.isnumeric() and y.isnumeric()):

print("Please enter numbers")

continue

# Now we know x and y can be safely casted to integers without crashing

x = int(x)

y = int(y)

if y == 0:

print("Your divisor cannot be zero")

continue

# If we pass all above checks, we can break out of the input loop

break

# Now we can safely divide by y without possibly causing ZeroDivisionError

print(x / y)

# Vocabulary

| Word | Definition |
| :-: | :-: |
| Loop | Used for repeating an action multiple times |
| Iterable | Something that can be stepped through element by element |
| Cycle/Iteration | A term for each time a loop runs |
| Loop Header | The part of a loop that determines the behavior of a loop |
| Loop Body | The statements that execute on each loop iteration |
| Defensive Programing | Making sure no invalid inputs from the user can crash your program; Use if and while statements to deal with invalid inputs |

# Python Concepts

| Word | Definition |
| :-: | :-: |
| while (condition): | A loop that will continue to cycle until the condition is False. Checks the condition before each iteration. |
| range(start, end, increment) | Iterates through a sequence of numbers |
| for val in seq: | A loop that cycles through each element in the sequence |
| break | Keyword that halts execution of a loop body and exits the loop; skips to the next line of unindented code |
| continue | Keyword that halts execution of a loop body and skips to the next cycle |

