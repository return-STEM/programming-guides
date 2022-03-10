# 7. 
Lists

Introduction to Python

return STEM;

Version 1

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

![](lists%5Clists0.png)

# Lists

![](lists%5Clists1.png)

* __Lists __ are an ordered collection of items.
* Each individual item inside the list is called an  __element__
* These items can be:
  * Integers/floats/booleans
  * Strings
  * Other data types
* For example:
  * If variables are boxes, a list would be a shelf which you place the boxes on.

![](lists%5Clists2.png)

![](lists%5Clists3.png)

![](lists%5Clists4.png)

# Why Use Lists?

* __Lists__  offer a useful way to:
  * Organize data where there is a variable number of entries
  * Perform the same task on a lot of grouped data
* For example, let’s say that I have a couple of lists to represent some information about a student at a school:
* It becomes much easier to find John’s average score, or find how many days he has missed class, etc.

name = "John"

grade = 8

scores = [98.0, 93.0, 87.5, 100.0]

attendance = [True, False, True, True, True]

# Syntax

Lists are declared like variables, but use square brackets [] around everything within them:

Each separate item inside the list is separated by commas.For example, here is a list containing integers from 0 to 9

list1 = ["cat", "dog", "cow"]# assigns the strings cat, dog, and cow to list1.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indices

* Each item in the list has an  __index __ that describes its position in the list
  * Like your position in line: if you're in the front, you're the first in line
* The first  __element __ in the list has index 0
  * This is called  __zero-indexing__ , where zero is the first value of a sequence of numbers (count starting from zero)

my_list = ['a', 'b', 'c', 'd']

0         1         2         3

# Negative indices

Positive indices reference elements from  _left to right_ .

Negative indices start from the opposite side.

my_list = ['a', 'b', 'c', 'd']

-4       -3       -2        -1

-1 is the  _last _ element of the list

-3 is the  _third last_  element of the list

# Getting Elements

* To retrieve a single list  __element__ , use the list name followed by the element's index in square brackets
* For example, my_list[1] returns 'b' because  'b' is the second (index 1) element in the list
  * x = list[0] sets variable x to 'a', the first element (index 0) in the list
* You can also set individual elements as well using this technique
  * my_list[2] = 'y' sets the third element (index 2) to 'y'
  * my_list now has the value ['a', 'b', 'y', 'd']

my_list = ['a', 'b', 'c', 'd']

0         1         2         3

# Slicing

* Just like in strings, lists can also be  __sliced__ :
* Slicing effectively  _creates a new list_  using a part of the original list, and the syntax looks like
  * It  __does not mutate__  the original list
* list_name[start:end] where Start and End are both indices
* Remember that Start is inclusive, but End is exclusive.
* Omitting End, like
  * list_name[start:] will make the code slice till the end of the list
* Meanwhile, omitting Start
  * list_name[:end] will make the code slice from the beginning

lst = [50, 70, 30, 20, 90, 10, 50]

print(lst[1:5])

>>> [70, 30, 20, 90]

![](lists%5Clists5.png)

# Indices Practice

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

animals = ['cat', 'dog', 'cow', 'sheep', 'pig']

fruits = ['apple', 'banana', 'lemon', 'tomato']

Using the declarations above, evaluate:

nums[1]

animals[4]

fruits[-2]

nums[-1]

fruits[3]

nums[1:5]

animals[0:2]

fruits[1:]

nums[:5]

# len()

To get the length of a list, you can use len().

This also works for strings:

my_list = ['a', 'b', 'c', 'd']

print(len(my_list))>>> 4

my_str = "Hello World"print(len(my_str))>>> 11

# Printing out lists

Lists can be directly printed out like this:

my_list = ['a', 'b', 'c', 'd']

print(my_list)

>>> ['a', 'b', 'c', 'd']

However, this might not be the best way you would like to present your information, since the format cannot be changed.

One way to print out lists in a better way is to  _iterate_  through each element and print them out individually.

# Iterating through lists

__You already know how to use for loops to go through a series of numbers, so you could do the following to iterate (go through all the elements) through a list:__

Iterating through lists can be useful to perform the same operation on every element of the list (such as print(), but could also be mathematical functions, checking for a condition, etc.)

my_list = ["orange", "apple", "pear", "banana", "kiwi"]

for i in range(0, len(my_list)):    print(my_list[i])>>> orange

>>> apple

>>> pear

>>> banana

>>> kiwi

# A shortcut using “for”

* There’s a shortcut for the code presented in the last slide:
* In the previous method, you were cycling through numbers, and using numbers to reference elements in the list
* Now you are directly cycling through the elements of the list without using indices
  * __You cannot use this type of loop to change the values inside a list.__

my_list = ["orange", "apple", "pear", "banana", "kiwi"]

for i in my_list:    print(i)>>> orange

>>> apple

>>> pear

>>> banana

>>> kiwi

# List Methods: .pop()

* To delete a single element from a list, you can use the .pop() function.
  * For example, letters.pop(2) deletes the item at the second index (3rd element).
* Notice that this shifts all indexes after the deleted item:
* Before: letters[0] = "a", letters[1] = "b", letters[2] = "c", letters[3] = "d"
* After: letters[0] = "a", letters[1] = "b", letters[2] = "d"

letters = ["a", "b", "c", "d"]

letters.pop(2)

print(letters)

__Output:__

['a', 'b', 'd']

# Examples

| Using for i in range(len(list)): | Using for i in list: | Output: |
| :-: | :-: | :-: |
| letters = [‘a’, ‘b’, ‘c’, ‘d’]<br />for i in range(len(my_list)):	print(my_list[i]) |  letters = [‘a’, ‘b’, ‘c’, ‘d’]<br /> for i in letters:   print(i) | >>> a<br />>>> b<br />>>> c<br />>>> d |
|  nums = [0, 1, 2, 3, 4]<br /> evens = 0<br /> for i in range(len(nums)):   if (nums[i] % 2 == 0):      evens += 1<br /> print(evens) |  nums = [0, 1, 2, 3, 4]<br /> evens = 0<br /> for i in nums:   if (i % 2 == 0):      evens += 1<br /> print(evens) | >>> 3 |
|  sum = 0<br /> vals = [98, 70, 100, 90]<br /> for i in range(len(vals)):   sum += vals[i]<br /> print(vals) |  sum = 0<br /> vals = [98, 70, 100, 90]<br /> for i in vals:    sum += i<br /> print(sum) | >>> 358 |

# List Methods: .append()

To add an element to the end of the list, you can use .append()Just like .pop(), use it after the name of the list, with the value you want to append.

For example, to append 'e' to the end of the list letters, you can use letters.append(‘e’)

letters = ['a', 'b', 'c', 'd']

letters.append('e')

print(letters)

>>> ['a', 'b', 'c', 'd', 'e']

# List Operators: * and +

Similar to strings, + and * can be used on lists

+ concatenates two lists together

* repeats a list multiple times

word = ['racecar']

print(word * 4)

>>>['racecar', 'racecar', 'racecar', 'racecar']

print(['racecar', 'bus'] + ['train'])

>>>['racecar', 'bus', 'train']

print([1, 2, 3] + [4, 5, 6])

>>>[1, 2, 3, 4, 5, 6]

# Notice that the values are not added together,  instead the lists are.

# in

* While in is a keyword when writing for loops, you can also use it to check whether an element is present in the list
  * in returns True if the value is in the list/string and False if the value is not

my_list = ['a', 'b', 'c', 'd']

print('a' in my_list)>>>True

This also works for strings:

my_str = "Hello World"print('o' in "Hello World")>>>True

# Tuples

* While you explore more libraries, you will find that many functions return a special data type called  __tuples__
  * Tuples are declared like lists, but use () instead of [].
* These data types behave like lists, but are  __immutable__  _ _ (cannot be changed).
* You cannot reassign values in a tuple, and the size of a tuple cannot change
  * Reference a tuple's elements just like you would in a list
  * Keywords like in and functions like len() can also be used on tuples
* You can use list() to convert a tuple to a list

my_tuple = (0, "apple", 2)

print(my_tuple[1])

>>> apple

animals = ("pig", "cow", "sheep")

print("cow" in animals)

>>> True

animals = ("pig", "cow", "sheep")

print(animals)

print(list(animals))

>>> ('cow', 'pig', 'sheep')

>>> ['cow', 'pig', 'sheep']

# Input with lists (on one line)

You cannot directly input lists with input(), since python believes that it is a string:

my_input = input("Enter input: ")print(type(my_input))Enter input: [1, 2, 3]

<class 'str'>

Instead, you can have the user input each element of the list with a space in between, using the .split() method on input().

my_input = input("Enter input: ").split()

print(type(my_input))print(my_input)Enter input: 1 2 3

<class 'list'>

['1', '2', '3']

If you put nothing in .split(), it will split the string by spaces. However, you can choose to include a string inside of .split() to tell it what to split by.

# Input with lists (on multiple lines)

Another method of inputting values into a list could be on multiple lines, using input() many times with a loop.

In this method, we can use a loop, after getting how many elements will be inputted.

reps = input("How many inputs? ")

my_list = []for i in range(reps):

ele = input()    my_list.append(ele)

print(my_list)

How many inputs? 3

1

2

3

>>> ['1', '2', '3']

# Casting an entire list

Notice that when you used input().split() to get inputs into a list from the user, everything was a string.

However, you can't use int() on input() like earlier, since int() cannot cast spaces and other formatting.

One way to do this is to  _iterate_  through each element, and change their type one by one.

vals = ["1", "2", "4", "3"]

print(vals)

for v in range(len(vals)):	vals[v] = int(vals[v])

print(vals)>>> ['1', '2', '4', '3']

>>> [1, 2, 4, 3]

# Outputting a list

When using print() on a list, you'll notice that it prints it with brackets and commas.

If you don't want that, you can do

str.join(list_name)

str is what should be in between the printed elements, usually ' ' for our purposes:

words = ["quickly", "scurry", "and", "find", "freedom"]

sentence = ' '.join(words)

print(sentence)

other_sentence = ', '.join(words)

print(other_sentence)

>>> quickly scurry and find freedom

>>> quickly, scurry, and, find, freedom

# Multidimensional Lists

* Lists can also have multiple dimensions (2D, 3D, 4D)
  * You can do this by putting lists inside of lists
* [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
  * This list has two lists inside of it that are two elements long (it is "2 by 2")
    * It behaves like a 2-dimensional table, with rows and columns
  * Elements can be addressed by indexing twice (my_list[row][col])
* Multidimensional lists can be used to model many real-world things
  * Tables and graphs are all 2-dimensional data that can be modeled with multidimensional lists
* You can also make 3, 4, and 5 dimensional lists (and so on)
  * Put list inside of lists inside of lists until you haveachieved the number of desired dimensions

|  | Element  0 | Element 1 |
| :-: | :-: | :-: |
| List 0 | "r1c1" | "r1c2" |
| List 1 | "r2c1" | "r2c2" |

# Multidimensional Lists: Example

You can represent a seating chart through a multidimensional list:

seating_chart = [

["None", "Tim", "Sally", "Ben"],

["Arnav", "Jason", "Mary", "Rav"],

["Aditya", "None", "Samantha", "Lee"]

["Joshua	", "Tyrone", "Adam", "Aarav"]

["Ethan", "Lilly", "Daryl", "Danny"]

]

# Print the person sitting in the first row and first column

print(seating_chart[0][0])

>>> None

# Print the person sitting in the third row and fourth column

print(seating_chart[2][3]

>>> Lee

# Iterating through multidimensional lists - Problem

* You can iteratively print values of a list:
  * for i in range(len(list)): print(i)
* However, if you did this using a multidimensional list, it would print simply the lists inside, rather than each individual value

two_d_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(two_d_list)):

print(two_d_list[i])

>>> [1,2,3]

>>> [4,5,6]

>>> [7,8,9]

# Iterating through multidimensional lists - Solution

* A nested loop can iterate through multidimensional lists
* The list [1,2,3] inside  __two_d_list__  is actually two_d_list[0]
  * Similarly, [4,5,6] is two_d_list[1] and [7,8,9] is two_d_list[2]
* An outer loop will retrieve the lists inside the combined list
* An inner loop will retrieve the values inside the inner lists
* The inner loop will iterate through two_d_list[i], or every list that is inside the combined list

two_d_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(two_d_list)):

for j in range(len(two_d_list[i])):

# New - prints on the same line

print(two_d_list[i][j], end = “ ”)

# Have we reached the last element?

# Then prints a new line

if j == len(two_d_list[i])-1:

print(“”)

>>> 1 2 3

>>> 4 5 6

>>> 7 8 9

# Iterating through multidimensional lists - Table

| Iteration | Value of loop variables | Value printed |
| :-: | :-: | :-: |
| 1 | i = 0, j = 0 | 1 |
| 1 | i = 0, j = 1 | 2 |
| 1 | i = 0, j = 2 | 3 |
| 2  | i = 1, j = 0 | 4 |
| 2 | i = 1, j = 1 | 5 |
| 2 | i = 1, j = 2 | 6 |

| Iteration | Value of loop variables | Value printed |
| :-: | :-: | :-: |
| 3 | i = 2, j = 0 | 7 |
| 3 | i = 2, j = 1 | 8 |
| 3 | i = 2, j = 2 | 9 |

![](lists%5Clists6.png)

![](lists%5Clists7.png)

![](lists%5Clists8.png)

# List Functions and Methods

| Function | Usage | Example |
| :-: | :-: | :-: |
| len() | Returns the length of the list | len([0, 1, 2]) returns 3 |
| max() | Returns the largest value of the list | max([1, 9, 3]) returns 9 |
| min() | Returns the smallest value of the list | min([1, 9, 3]) returns 1 |
| .pop() | Removes the element at the specified index, then returns it | [1, 2, 3].pop(1) returns 2and changes list to [1, 3] |
| .append() | Adds the element to the end of the list | [1, 2, 3].append(4) changes list to [1, 2, 3, 4] |
| .sort() | Sorts the list from least to greatest | [5, 6, 2].sort() changes list to [2, 5, 6]  |

# Vocabulary

| Word | Definition |
| :-: | :-: |
| List | An organized and mutable (changeable) sequence of items |
| Tuple | An organized but immutable (unchangeable) sequence of items |
| Element | The items inside of a list (like each shelf in a bookshelf) |
| Index | The position of an element inside of a list |
| Slicing | The process of creating a list by taking a part of one that already exists |
| Mutable/Immutable | An object that can be changed / cannot be changed.<br />Lists are mutable, tuples are immutable. |

