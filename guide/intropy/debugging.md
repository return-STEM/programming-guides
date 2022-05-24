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
