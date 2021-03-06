
In this course, you will learn the concept of object-oriented programming, which will take your basic skills to the next level. Since all programming is built on the basics, in this first lesson we will cover some key points of programming as a refresher to you. 

Many students that learn complex concepts struggle not with the new material, but with the fundamentals. When in doubt, go back and relearn the fundamentals. 

> This guide contains many links to the corresponding Introduction to Python material-if you ned a refresher, feel free to click the link and it'll bring you to the topic.

# Variables and Data Types

Variables [store information](/intropy/variables#storing-information), which can have a variety of different [data types](/intropy/variables#data-types):

|Data Type | What they represent|
|--- | ---|
|int | Positive or negative whole numbers |
|float | Positive or negative decimal numbers |
|bool | True or False | 
|str | Unicode characters |

Aside from this, there are also more complex data types that represent multiple pieces of information, called **data structures**:  
  
|Data Type | What they represent | 
|---|----|
| [list](/intropy/lists) | Mutable collection of data | 
| [tuple](/intropy/lists#tuples) | Immutable collection of data | 
| set | Immutable, unindexed collection | 
| dict | collection of data in key:value pairs |

Data types are set when the variable is declared, a variable can be [**casted**](/intropy/variables#casting) into another data type with the typecasting functions:

| Function | Result | Behavior with: |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
|  |  | int | float | bool | str |
| int() | int | Already an int | int(5.3) → 5 | int(True) → 1<br />int(False) → 0 | int("10") → 10 |
| float() | float | float(5) → 5.0 | Already a float<br /> | float(True) → 1.0<br />float(False) → 0.0 | float("3.5") → 3.5 |
| bool() | bool | bool(5) → True<br />bool(0) → False | bool(5.3)→ True<br />bool(0.0)→ False | Already a bool | bool("pie") → True<br />bool("") → false |
| str() | str | str(5) → "5" | str(5.3) → "5.3" | str(True) → "True"<br />str(False)→ "False" | Already a str |

You may retrieve the type of a variable with `type()` .

```python
x = 5

print(type(5))
>>> <class 'int'>
```

# Console I/O and String Manipulation
Text is displayed on the [console](/intropy/consoleio#the-console) using `print()`, and can be [collected through `input()`](/intropy/consoleio#using-input). 

`input()` can take one parameter, the prompt of the input, like this: 

```python
name = input("What's your name?")
>>> What's your name? _  
```

The `print` function can take the following parameters:  

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

> `objects` are the data you want to print. You can put multiple objects, separated by commas.
> 
> `sep` is placed between each object, if multiple are specified. Default to a space (`' '`)
> 
> `end` is placed after the objects that are printed. Defaults to a newline (`'\n
> '`)
> 
> `file` is the placed the data is printed to Default to `sys.stdout` (ther terminal
> 
> `flush` specifies whether to flush the `stdout` buffer and display the contents to the screen immediately. Defaults to `False`, and the buffer is flushed every newline. You shouldn't need to touch this, but if you're curious, [read more here](https://www.geeksforgeeks.org/python-sys-stdout-flush/)

The `print()` you are used to uses all these default parameters, so when you print multiple strings like this: 

```python
print("Green Eggs", "and", "Ham)
>>> Green Eggs and Ham
```

  

[Strings can be manipulated](/intropy/consoleio/string-manipulation) in the following ways: 

## Concatenation (`+`)
You can append one string to another using the `+` operator. 

```python

a = "Tree"  
b = "House"

print (a + b)
>>> TreeHouse
```

## Repetition (`*`)
You can append one string to itself `n` times by using the `*` operator. 

```python

a = "Tree"

print(a * 3)
>>> TreeTreeTree
```

## Accessing a character ([Indexing](/intropy/consoleio#indices-and-strings))

You can access a character at the nth index of a string with indexing operator `[]`

```python
a = "Tree"

print(a[2])
>>> e
```

### Slicing
You can access multiple characters from a string to create a slice of the string, from index `a` to `b`. 

Remember that the `start` index is inclusive of the value, but the `end` is exclusive of the value. 

Finally, when the start is excluded, Python assumes the start is 0.

If end is excluded, Python assumes the end is the end. 

```python
a = "TreeHouse"

print(a[:3])
print(a[2:6])
print(a[2:])
>>> Tre
>>> eeHo
>>> eeHouse
```

## [String Formatting](/intropy/consoleio#indices-and-strings)
For Python 3.6+, you can use f-strings (Currently, we're on 3.10, but sometimes you might see 3.5 on old websites). 

They're declared like this:  
```
f"content"
```

When you want a variable to used in them, you can include the name in curly braces `{}`. 

For example:  
```python
Name = "Alex"
Color = "Green"

print(f"My name is {Name} and my favorite color is {Color}")
>>> My name is Alex and my favorite color is Green  
```

Alternatively, you can use `.format()` or `%s`, which look like this:

```python
print("My name is {} and my favorite color is {}".format(Name, Color)
print("My name is %s and my favorite color is %s" % (Name, Color)")
```

Which accomplishes the same task as above. 

Here's a table of escape characters:

# Basic Operations
  
Python has many operators, including the [four basic arithmetic operators](/intropy/arithmetic#doing-math-in-python):

| Python Syntax | Operation | Math Symbol | Example | Result |
| :-: | :-: | :-: | :-: | :-: |
| `+` | Addition | + | `5 + 2` | `7` |
| `-` | Subtraction | − | `6 - 4` | `2` |
| `*` | Multiplication | × | `4 * 3` | `12` |
| `/` | Division | ÷ | `8 / 4` | `2` |

Here are some [other ones](/intropy/arithmetic#advanced-operators) that you might not be as familiar with:

> **Integer Division** always rounds the result down, truncating the decimal
> 
> **Modulus** retrieves the remainder of an integer division
  
| Python Syntax | Operation | Math Symbol | Example | Result |
| :-: | :-: | :-: | :-: | :-: |
| `//` | Integer Division | None | `13 // 4` | `3` |
| `%` | Modulus | `%` | `17 % 4` | `1` |
| `**` | Exponent | Superscript | `5 ** 2` | `25` |

> Don't forget the order of operations--more info [here](/intropy/arithmetic#order-of-operations)

Along with this, here are some useful functions, some of which are contained in [the `math` module](/intropy/arithmetic#the-math-module). 

As a reminder, you can use the `math` module by including `import math` at the start of the program. 

Function | Behavior | Example
--- | --- | ---- 
`round(number, digit=0)` | Rounds number to the digit th decimal place. | round(3.1415, 2) → 3.14 | 
`math.sqrt(x)` | Returns the square root of x as a float | math.sqrt(4) → 2.0 | 
`math.fabs(x)` | Returns the absolute value of x as a float | math.fabs(-3) → 3.0 |
`math.factorial(x)` | Returns the factorial of x | math.factorial(5) → 120 | 
`math.gcd(x, y)` | Returns the greatest common divisor of x and y | math.gcd(75, 35 ) → 5|
`math.pi`| Evaluates the digits of pi | math.pi → 3.141592653589793 | 
`math.e` | Evalues the digits of e |  2.718281828459045 | 

Additionally, you can generate random numbers using the `random` module. 

Function | Behavior | Example 
---|---|--
`random.random()` | Returns a random float between 0 and 1 | random.random() → 0.15074098317978457 | 
`random.uniform(x, y)` | Returns a random float between x and y | random.uniform(1,5)
→ 2.8951547807157176 | 
`random.randint(x, y)` | Returns a random integer between x and y | random.randint(x, y) → 4| 

  
# Conditionals

An [`if` statement](/intropy/conditionals#ifelse-structure) looks like this: 

```python

if (conditional1):
	do_something()
elif (conditional2):
	do_something_else()
else:  
	do_a_thing()
```

  
Remember that you may use the following [comparison operators](/intropy/conditionals#comparison-operators) to compare the value of two variables and return a boolean result:

| Symbol | Operator | Definition | Example |
| :-: | :-: | :-: | :-: |
| ==  | Equal To  | If the values of two operands are equal, then the condition becomes true. | (a == b) is not true. |
| !=  | Not Equal To | If values of two operands are not equal, then condition becomes true. | (a != b) is true. |
| > | Greater Than | If the value of left operand is greater than the value of right operand, then condition becomes true. | (a > b) is not true. |
| < | Less Than | If the value of left operand is less than the value of right operand, then condition becomes true. | (a < b) is true. |
| >= | Greater Than or Equal To | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true. |
| <= | Less Than or Equal To | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | (a <= b) is true. |

And these [logical operators](/intropy/arithmetic#logical-operators) to create composite comparisons:

  
| Operator | Definition | Example |
| :-: | :-: | :-: |
| `and` | If both the operands are true then condition becomes true. | True and True → True |
| `or` | If any of the two operands are non-zero then condition becomes true. | True or False → True |
| `not` | Used to reverse the logical state of its operand. | not (True or False) → False |

# Loops
[`while` loops](/intropy/loops#the-while-loop) repeat till their `condition` is met, and look like this:

```python

while (condition):  
repeat_something()

repeat_more()

```

The logic used in this loop: 

```python

while a < 10:

print(b)

a += c

```

![](review/loops-6-flowchart.png)

[You can use `break` to end a `while` loop early, or use `continue` to skip the current iteration.](/intropy/loops#break-and-continue)

[`for` loops](/intropy/loops#the-for-loop) instead iterate through an iterable, such as strings, lists, range(), and others: 

```python
for element in iterable: 
	body_of_code() # We can use 'element' inside this code
```

`continue` and `break` behave as normal with `for` loops. 

# Lists

Lists are [ordered collections of items](/intropy/lists#what-are-lists): 

```python
my_list = ["cat", "dog", "bird"]
```

Lists are [zero-indexed](/intropy/lists#indices), meaning you may access the first element using the indexing operator `[]` with `0`. 


```python
my_list = ["cat", "dog", "bird"]
print(my_list[0]) # Access first (zeroeth) element of list
>>> cat
```

While positive indexes start from left to right, [negative indices](/intropy/lists#negative-indices) go from right to left. 

```python
my_list =  ["cat", "dog", "bird"]
print(my_list[-1]) # Last element of list
>>> bird
```

Just like strings, you can [slice lists](/intropy/lists#list-slicing), with similar behavior. 

When a list is sliced, a new one is formed using a part of the original list. List slicing does not mutate the original.

You can slice them like this:  
```python
list_name[start:end]
```

> Don't forget: `start` is inclusive, but `end` is exclusive

If `start` is omitted, it defaults to 0
if `end` is omitted, it defaults to the end of the list `len(my_list)`

%%TODO replace this graphic%%

![](https://lh3.googleusercontent.com/y8_R-45bwK-EjdPJXnshCk7iBDOb0qqVhpQ9jrA1P-LQ1oDPQs4QgVCL_lKIOrjoBc2OXpveEOrEXp4g8d2NuD0MHRvWVuyMGmTBwSWK8v-vlnt07iWN4JTD0MQrcRbKX2fgoV7f)

Here's a table of useful [list functions and methods](/intropy/lists#list-methods--operations): 

Function | Usage | Example
---|---|---
 [len()](/intropy/lists#len) | Returns the length of the list | len([0, 1, 2]) returns 3
max() | Returns the largest value of the list | max([1, 9, 3]) returns 9
min() | Returns the smallest value of the list | min([1, 9, 3]) returns 1
.pop() | Removes the element at the specified index, then returns it | [1, 2, 3].pop(1) returns 2 and changes list to [1, 3]
.append() | Adds the element to the end of the list | [1, 2, 3].append(4) changes list to [1, 2, 3, 4]
.sort() | Sorts the list from least to greatest | [5, 6, 2].sort() changes list to [2, 5, 6] 

Lists can also contain lists, creating multi-dimensional lists: 

```python
tic_tac_toe = [['X', 'O', 'X'], ['X', '  ', 'O], ['O', 'X', 'O']]
								 
# Looks like this:
# [['X', 'O', 'X'], 
#  ['X', '  ', 'O], 
#  ['O', 'X', 'O']]
```


# Functions
You can [declare your own functions](/intropy/functions like this: 

```python
def func (params):  
	# instructions 
```

[When you want to call it](/intropy/functions#calling-functions), simply use its name followed by its parameters. 
You can also assign default parameters that are optional. 

```python

def greet_me(name, times = 1, greeting = "Good Morning"):
	for i in range(0, times):
		print(f"{greeting}, {name}!"

greet_me("Sam", greeting = "Hello") # times still defaults to 1
>>> Hello, Sam!
```

When we pass arguments to a function, we do it in two ways: [pass by value](/intropy/functions#pass-by-value) and [pass by reference](/intropy/functions#pass-by-reference):

Integers, floats, booleans, and strings are primitive in Python. This means that when we pass them to a function, the function receives a copy of the value. When we change the value inside the function, the original variable is not affected. 

However, non-primitive types (everything else) are passed a reference to the object, meaning those changes will affect the original variable. 

![](review/functions-8.png)

| \n | Starts a new line | print("Hello\nWorld")<br /><br />> Hello<br />> World |
| :-: | :-: | :-: |
| \b | Backspace | print("Hello \bWorld")<br /><br />> HelloWorld |
| \t | Works like a tab | print("Hello\tWorld")<br /><br />> Hello    World |
| \\ | Acts as a regular backslash | print("Ok\\")<br /><br />> Ok\ |
| \' | Acts as a regular single quote (apostrophe) | print('Rob\'s World')<br /><br />> Rob’s World |
| \" | Acts as a regular double quote | print("He said \"try to\"")<br /><br />> He said "try to" |