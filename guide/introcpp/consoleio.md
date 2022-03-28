
# Console Input/Output

Every program you will write will take some form of input, and then give you back some output. In this lesson, you will learn how to take input and output information through the console. 

You've already learned some of this - in your first ever program, you outputted the text Hello World to the console. Now, you'll learn more behind console output, and learn how to accept input from the console. 

## Console Output

You've learned plenty of data types in the previous lesson, [variables](https://guide.returnstem.org/introcpp/variables?).
These data types can represent a variety of different numbers and other useful values, but they don't represent a really important type of data. All text, which can include characters (letters), words, sentences, and paragraphs, can be represented using strings. Strings are identified by double quotes surrounding them, and can contain any characters.  
For example, a string might look like this: 

`"I woke up at 8 am today."`

When you want to output text to the console, you will need to make it a string. 

If you don't include it as a string, C++ will think they are other variables and your code will not compile. 

## The `String` class

Strings can be defined like other data types, like this:
```cpp
string str1;
```
However, you must include the string header file to do this, just like <iostream>.
```cpp
#include <iostream>
#include <string>
```
You can define strings in different ways:
```cpp
string s = "a string";
```
Or simply,
```cpp
string s
```
If you don't want to define it yet. 

## Escape Characters

Notice that because we open and close strings with `"`, when we want to use the `"` character in our strings, C++ will think you are making two strings, like this:
```cpp
cout << "Mary said, "hello everyone" on tuesday";
```

Thankfully, we can use escape characters to tell C++ that our quotes `"` are not part of declaring the string. 
When we use the backslash character, `\`, followed by another, C++ considers at as one escape character. 
To use quotes in your string, for example, you would use `\"`. 

Escape characters can also be used for other purposes: for example, a backslash followed by an n, `\n`, signifies a newline character. When C++ sees this character, it will cause the following text to be printed on the line below the current one. 

```cpp
#include <iostream>


using namespace std;

int main()
{
    cout << "Hello \nWorld";
}

>>>Hello
>>>World
```


Similarly, `\t` is a tab character, which moves the text to the next tab position. It doesn't add a new line. 

Finally, if we want to use the \ character in a string, we can use two of them in a row: `\\`. 
```cpp
cout<<”\”May the Force be with you\””;
```
Common escape characters: 
| Escape character | Function | 
| --- | --- | 
| `\n` | Outputs a newline | 
| `\t` | Outputs a tab | 
| `\’` | Outputs a single quotation mark | 
| `\”` | Outputs a double quotation mark | 
| `\\` | Outputs a slash | 



## The `cin` statement

Now that we have gone over outputting something to the console for the user to see, we will learn how to take an input from a user. The command cin is used for this task. It takes an input through the standard input device, usually a keyboard, and stores it in a predefined variable. A stream extraction operator (>>) goes between the variable name and the cin statement. 

Notice that for cin, we use >> operators, while for cout we use <<. 
```cpp
int age;
cin >> age;
```
When using cin, the user will be prompted to give input on the console. You may type anything into it, and submit your input by pressing `Enter` or `Return`. 

Consider the following code: 

```cpp
#include <iostream>

using namespace std;
int main()
{
    int age; 
    cout << "What is your age? ";
    cin >> age;
    cout << "You are " << age << " years old. " << endl;
}

```
When run, this code will prompt the user for their name. Notice that it does not print what comes after it till you give it input. 

Try asking some questions to the user, collecting the input, and displaying the input in some way using `cin` and `cout`. 

If we want to accept multiple inputs on the same line and store them in multiple variables, we do something similar. 

```cpp
#include <iostream>

using namespace std;
int main()
{
    int month, day;
    cin >> month >> day;
    cout << "The day is " << day << " and the month is " << month << endl;
}
```

The inputs are separated by spaces. 

However, notice that in these examples, we all used the `int` data type. When you try to input something that is not an `int` into a cin for a `int` variable, it will not work well. 

Here's another example, this time accepting a string:

```cpp
#include <iostream>
#include <string>

using namespace std;
int main()
{
    string name;
    cout << "What is your name? ";
    cin >> name;
    cout << "Hello, " << name;
  
}
```


## I/O Manipulation

The basic format of the cin statement isn’t always useful because we might want to receive the input in other ways. For this reason, there are many functions in C++ that help with this. 

`getline(cin, str)`  receives input from the console and stores it inside a variable (in this case, called `str`). It performs a similar function to `cin`, but can take in input separated by spaces. For example, in this program, 
```cpp
#include <iostream>
#include <string>

using namespace std;
int main()
{
    string name;
    cout << "What is your name?";
    cin >> name;
    cout << "Your name is " << name;
}

>>> What is your name? 
>>> John Smith
>>> Your name is John
```
If the user inputs their full name (something like "John Smith"), only "John" will be stored inside `name`. This is because cin stops reading input after a space. 

However, `getline` stops at a new line, or when you press `Enter` on your keyboard.

The same program using getline would look like this:
```cpp
#include <iostream>
#include <string>

using namespace std;
int main()
{
    string name;
    cout << "What is your name?";
    getline(cin, name);
    cout << "Your name is " << name;
}
>>> What is your name? 
>>> John Smith
>>> Your name is John Smith
```

Another function similar to `cin.get()` is the `cin.peek()` function. Instead of moving through the input stream and storing characters in variables, the function just peeks at the next character and stores it in a variable. Since the function doesn’t move through the input stream, using the `cin.peek()` function multiple times won’t move through the characters, it will just stay at the next character. Another important thing to remember is that this function doesn’t accept a parameter, you have to set it equal to a parameter like this: `ch = cin.peek()`.


`cin.ignore(n, ch)` is used to ignore characters in an inputted string until either n characters have been read or a certain character (ch) has been read (whatever comes first). `cin.get()` is used after this to show what character we are at.


## `<iomanip>`

Before you use any of the following tools, remember to include the `<iomanip>` library, like this: 
```cpp
#include <iomanip>
```

`setprecision()` is used to manage the number of digits that is in an output. For example, if we wanted to output a long number rounded to 3 digits, we pass 3 as the parameter to `setprecision()`. 
```cpp
#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
  float pi = 3.1415;
  cout << pi << endl;
  cout << setprecision(3) << pi << endl;
}
>>> 3.1416
>>> 3.14
```
After settings the precision to 3, only 3 digits of pi are displayed. 

Another function that deals with outputting a certain number of digits is fixed. It is used along with `setprecision()` and rounds the number of digits after the decimal point. If we wanted 2 digits after the decimal point, we would pass 2 as the parameter. 

```cpp
#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
  float profits = 300.75;
  cout << profits << endl;
  cout << fixed << setprecision(1) << profits << endl;
}
>>> 300.75
>>> 300.8
```
`showpoint` is used to display values with decimal points, even if it is a zero. It displays decimal points to match the precision of the stream, set by `setprecision`. 

```cpp
#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
  cout << fixed << showpoint << setprecision(3) << 10.0 << endl;
}
>>> 10.000
```

