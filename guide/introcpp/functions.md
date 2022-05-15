You've already used functions in the past. One of their biggest advantages is reusability - for example, the `<cmath>` header file contains many useful functions, like `ceil`, `floor`, and `round`. Because these functions are already defined, you don't need to rewrite the code needed to do this. Instead of implementing logic to round a number, it was already defined - you won't need to do it yourself.

In this lesson, you will learn how to write your own functions. 

# What Are Functions?

Functions are just blocks of code that are predefined, and can be reused for your purposes. 

You've already used many functions in the past: 
- `ceil`
- `floor`
- `round`

There are many more functions that you will learn about and use, which will be covered in the next lesson.

## Declaring Functions

The syntax of a function looks like this:
```cpp
returnType functionName(type parameter1, type parameter2, …) {
	// code that you want 
	return value;
}
```
The code you write is really just something that takes in input, and then returns some output back to you for you to see. Functions are similar to that. 
Functions can take in (be passed) values called parameters, which it will then process and return a value. 

You'll need to specify the type of the return value, as well as the name of the function, so that it can be called later. 

Additionally, functions should be declared outside of your `main()` function. 
Functions can be called in a more simple manner, that you're probably familiar with already:

Consider our own implementation of the `round()` function:

```cpp
int round(float n)
{
  if (n > 0.0)
    return (int)(n + 0.5);
  else
    return (int)(n - 0.5);
}
```
`round()` returns the nearest integer to `n`. 
We can call `round()` like this:
```cpp
#include <iostream>
using namespace std;
int round(float n)
{
  if (n > 0.0)
    return (int)(n + 0.5);
  else
    return (int)(n - 0.5);
}
int main() {
  cout << round(5.6) << endl;
}

>>> 6
```

# Parameters and Arguments

When talking about functions, you will hear the words parameter and argument used almost interchangeably - but they're not the same thing. 
> Parameters are like placeholders for the values that you will pass to the function, while arguments are the values actually passed to the function
```cpp
void example(int param1, int param2) // Parameters
{
	cout << param1 + param2;
}

example(5, 6) // Arguments
}
```

## Passing by Value

Sometimes, we when pass values to a function, nothing outside the function is changed. When a variable is passed to a function, it isn't actually getting passed - C++ makes a copy of that function and then uses that in the code. 

This is called _passing by value_.

