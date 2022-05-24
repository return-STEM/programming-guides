When programming, you will inevitably come across errors. Learning how to deal with errors is an important skill you will need to learn, especially when writing larger programs. In fact, programmers spend more time debugging code than writing it.

# What are errors?

An error is a problem that prevents a program from working as intended. They can arise through typos, lack of attention, or logical issues. 
To remove these errors, programmers debug their code, which is the process of removing/fixing errors ("bugs") in their software
The process of debugging looks something like this:
1. Locate the error
2. Identify the type of error that is present
3. Find ways to correct/remove that error
4. Retest program to see if error has been successfully fixed

Don't feel discouraged if you make mistakes while you write code: errors are common, and everyone makes them. The important thing is to learn _how_ to fix them.

# Types of Errors

There are three general types of errors in programming: 
1. Syntax
2. Runtime
3. Logical

## Syntax Errors

Syntax errors occur when Python can't understand specific lines of code: it can only understand very specific commands, and isn't good at inferring what you mean from your code.

Generally, syntax errors are easy to fix and easy to spot. A syntax error to Python is like if you said a sentence that doesn't make sense:

_cat me the monkey dog_

If someone said that to you, you would always respond with, "what does that mean?" 

Python thinks in a similar way. When you type something that doesn't make sense to them, you'll get an error. 

Python will notify from you of these errors when you try to run the program. Generally, the format will look like this:

```
Error location
Line of code

SyntaxError: <error>
```
Consider this flawed code:
```python
temperature = 20
if temperature == 10:
    print("10)

# An error is caused as there is no double quote to close off the text in the print statement. 
```
There's an error because a double quote is missing, so Python won't understand the code. Therefore, it will return an error.

Generally, if you type something that is incorrect, your IDE (the environment you program in, like VScode, Pycharm, Repl, etc.) will put a squiggly line under the faulty code.

## Runtime Errors

Runtime errors occur when while the program is trying to run. Runtime errors occur when the program is telling Python to do something that it cannot do, but it technically still grammatically correct. 
Examples:
- Trying to index an integer with []
- Attempts to perform mathematical operations on data of the wrong type (strings)
- Dividing by zero

For example, if you tell a chef to peel flour, they will tell you that they can't do it. It's an error, because you _can't_ peel flour. Or, for example, you can't add the word "apple" to the number 5. It's not possible to do. 

You can look at the specific exceptions [here](https://docs.python.org/3/library/exceptions.html)

One of the runtime errors you might encounter is a `ZeroDivisionError`:

```python
print(5/0)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Runtime errors can sometimes be easy to fix, because they might be typos. 
Runtime errors might also come from invalid input. 

Consider the following code:
```python
# This program prints the quotient of 
# two numbers 

a = int(input("Enter the divisor: "))
b = int(input("Enter the dividend: "))

c = a/b

print(f"Quotient: {c}")
--------------------------
Enter the divisor: 5
Enter the dividend: 0

Traceback (most recent call last): 
    File "main.py", line 4, in ,module.
        c = a/b
ZeroDivisionError: division by zero
```

The program has correct syntax and can execute. 
However a runtime error has occurred!
If we look at line 4, where the error occurred, there is no division by 0 occurring there on the surface
Let's trace through the code:
In line 1, we store  the int 5 in variable a
In line 2, we store the int 0 in variable b
In line 4, we divide a and b, or 5/0
A number cannot be divided by 0. 
The error came from b being assigned to 0 through the input, which would result in the variable a being divided by 0. 

One of the solutions to this is to use _defensive programming_.
We can add code that prevents `b` from ever being assigned the value 0.
This effectively prevents ZeroDivisionError.
When the user inputs 0, the program:
- Asks the user to input the dividend again 
- Reminds them that the dividend cannot be 0

```python
# This program prints the quotient of
# two numbers 

a = int(input("Enter the divisor: "))

while True: 
    b = int(input("Enter the dividend: "))
    if b == 0: 
        print("The dividend cannot be 0")
        continue
    break

c = a/b

print(f"Quotient: {c}")
--------------------------
Enter the divisor: 5
Enter the dividend: 0
The dividend cannot be 0
Enter the dividend: 5
Quotient: 1
```

## Logical Errors
Logical Errors are the trickiest errors to find and fix. They are "silent", so Python does not help you fix them.
Logical errors occur when the code itself runs perfectly fine, but it does not produce the result you want it to.
Python only knows what it is told to do: it is doing its job!
These errors can arise from typos or incorrect program design
Examples:
- Inputting an incorrect, but valid variable name
- Indenting to a wrong but valid level
- Not respecting order of operations but still producing valid code
- Using a wrong but valid operator
All of this code will run, but it will not produce the result you want it to!

For example, if you gave a chef to make a pie and you gave it a cake, it would just make a pie. But you don't want that, so that's not good!

Consider the following faulty code:
```python
# This is a program that outputs the 
# product and sum of a and b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a * b

print(f"Product: {c}")
c == a + b
print(f"Sum: {c}")

# The second "assignment" to c is not actually an assignment, it is an equality
```




