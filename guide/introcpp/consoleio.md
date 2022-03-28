---
slides:
""
handout:
""
---
# Console Input/Output

Every program you will write will take some form of input, and then give you back some output. In this lesson, you will learn how to take input and output information through the console. 

You've already learned some of this - in your first ever program, you outputted the text Hello World to the console. Now, you'll learn more of what exactly cout does along with how to C++ handles console input.

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

However, you must include the string header file to do this, just like `iostream`. Luckily for us, we don't have to include the string header if we already included the iostream header. This is because `iostream` already includes the `string` header for us.

```cpp
#include <string>
```

You can declare strings in different ways:

```cpp
string s = "a string";
```

Or simply,

```cpp
string s;
```

If you don't want to initialize it yet. 

## Escape Characters

Notice that because we open and close strings with `"`, when we want to use the `"` character in our strings, C++ will think you are making two strings, like this:

```cpp
cout << "Mary said, "hello everyone" on tuesday";
```

Thankfully, we can use escape characters to tell C++ that our quotes `"` are not part of declaring the string. When we use the backslash character, `\`, followed by another, C++ considers at as one escape character. To use quotes in your string, for example, you would use `\"`. 

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

Finally, if we want to use the `\` character in a string, we can use two of them in a row: `\\`. 
```cpp
cout << "\"May the Force be with you\"";
```
Common escape characters: 
| Escape character | Function | 
| --- | --- | 
| `\n` | Outputs a newline | 
| `\t` | Outputs a tab | 
| `\’` | Outputs a single quotation mark | 
| `\”` | Outputs a double quotation mark | 
| `\\` | Outputs a back slash | 
| `\?` | Outputs a question mark |

## The `cin` statement

Now that we have gone over outputting something to the console for the user to see, we will learn how to take an input from a user. The object cin is used for this task. It takes an input entered in the console, and stores it in a variable. We use the `>>` operator to between the variable name and the cin statement. 

>Notice that for cin, we use `>>`, while for cout we use `<<`. To remember this, you can think of it as `<<` feeding the data into the console with cout and `>>` retrieving the data from of the console for cin. The direction of it follows the pattern.

If we wanted to  take the console input and store it into a variable of the `int` type, we would use the following code.

```cpp
int myVar;
cin >> myVar;
```

When using cin, the program will wait until the user types the input and presses the `Enter` or `Return`  key. Be careful, `cin` does not give a prompt or any text that it is waiting for an input. Instead, we have to use `cout` to remind the user that the program is waiting for an input.

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

If we want to accept multiple inputs in one `cin` statement, we can separate the different variables with the `>>` just as we would use `<<` for `cout`. 

```cpp
#include <iostream>

using namespace std;
int main()
{
    int month, day;
    cout << "Enter the month and day: ";
    cin >> month >> day;
    cout << "The day is " << day << " and the month is " << month << endl;
}
```

When taking in multiple variables of input, the user can either enter data like

```cpp
>> 8
>> 24
```

or

```cpp
>> 8 24
```

`cin` will separate different inputs with spaces or newlines (pressing `Enter`), but it will only take in what you have typed into the console after you press your `Enter` key.

However, notice that in these examples, we all used the `int` data type. When you try to input something that is not an `int` into a cin for a `int` variable, you program will not output what you entered. 

Here's another example, this time accepting a string:

```cpp
#include <iostream>

using namespace std;
int main()
{
    string name;
    cout << "What is your name? ";
    cin >> name;
    cout << "Hello, " << name << endl;
  
}
```


## I/O Manipulation

The basic format of the cin statement isn’t always useful because we might want to receive the input in other ways. For this reason, there are many functions in C++ that help with this. A function is a piece of code that can take inputs and run some code based on that. We will learn more about functions and how to create your own functions in a later lesson.

If you wanted the user to input a sentence and get that input with `cin`, you would be unable to do so. Consider the following code and respective input/output:

```cpp
#include <iostream>

using namespace std;
int main() 
{
	string sentence;
	cout << "Please enter a sentence: ";
	cin >> sentence;
	cout << "This is the sentence you inputted: \"" << sentence << "\"" << endl;
}

>> This is my sentence.
>> This is the sentence you inputted: "This"
```

Remember how before we said that you could input the values for multiple variables in one line by separating them with a space, and then it takes them all in when you press enter. That's what happened just now, and since "this" and "is" were separated by a space, `cin` thinks they should go into separate variables.

Now, we clearly didn't give `cin` more than one variable to put our data into. So shouldn't `cin` be smart enough to realize what we are trying to do and just put it all in the sentence variable? Well, we have to understand that `cin` isn't programmed to work like that.

%%TODO go on to more detailed information about the input buffer, etc%%

The solution to the aforementioned problem is the function `getline(cin, str)`. Functions are ways to call code that can take inputs and give outputs. We will learn more about them and how to create them in a later lesson. For now, just know that we write them like `nameOfFunction(input1, input2)`. We could have no inputs in the parenthesis, or how man ever we need depending on the function. In the case of `getline`, it takes two inputs, the `cin` object and a string variable to write the input to. 

`getline` works a little differently than using `cin`. It will read your input until it reaches a `\n` character which we input to the console by hitting the `Enter` key. Unlike `cin`, `getline` will move to the character after the `\n` character in the stream buffer.

The same program, but using getline would look like this:

```cpp
#include <iostream>

using namespace std;
int main() 
{
	string sentence;
	cout << "Please enter a sentence: ";
	getline(cin, sentence);
	cout << "This is the sentence you inputted: \"" << sentence << "\"" << endl;
}

>> This is my sentence.
>> This is the sentence you inputted: "This is my sentence."
```

Another function similar to `getline` is the `cin.peek()` function. Instead of moving through the input stream and storing characters in variables, the function just peeks at the next character and stores it in a variable. Since the function doesn’t move through the input stream, using the `cin.peek()` function multiple times won’t move through the characters, it will just stay at the next character. Another important thing to remember is that this function doesn’t accept any parameter. However, you have to store the returned (outputted) character in a `char` variable: `char ch = cin.peek()`.

%%TODO example of cin.peek()%%

`cin.ignore(n, ch)` is used to ignore characters in an inputted string until either n characters have been read or a certain character (ch) has been read (whatever comes first). 

%%TODO explanation of phantom newline problem and use of cin.ignore() to solve it%%

%%TODO explain cin.fail() and cin.clear()%%

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

>`setprecision` **DOES NOT** say how many digits to round to, but how many digits to display. 

Another function that deals with outputting a certain number of digits is `fixed`. It is used along with `setprecision` and rounds the number of digits after the decimal point. When we use `fixed`, `setprecision` will act like a round to `x` number of digits function.

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

%%TODO explain setw%%
%%TODO explain setfill%%