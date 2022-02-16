# Control Structures: Conditionals

Up until now, you've learned to make **linear** C++ programs, where the program executes from top to bottom. Sometimes the program will take a break to ask for user input, but the way it runs is pretty straightforward.

**Control structures** change that up a bit. This lesson, we'll be showing you how to write programs that decide what code to run. This is called the **control flow** of the program, or which "path" the program takes. Think of it like a fork in the road–you decide to either go right or left. This brings us to our first challenge: figuring out how our computers make decisions.

# How Do Computers Make Decisions?

Computers make decisions a little differently from humans. When I choose what I'll eat for lunch, I need to ask myself a few questions: What do I want? How much am I willing to spend? How convenient is it for me to get it? All these questions have an infinite number of answers.

However, as you might remember from lesson 2, computers operate on an on-or-off basis–this means that each question can only have two answers, `true` or `false`, or 0 or 1. In C++, there's a data type for that–the **boolean**! In summary, each question our program has to answer needs to have a boolean answer, either `true` or `false`.

# Relational Operators

Thankfully, C++ gives us a few predefined "questions" in the form of **relational operators*.*** These compare two pieces of data and give us a **boolean result**–exactly what we're looking for! For simplicity's sake, we will only use relational operators on numbers for now, so we will be comparing the values of numbers. You might recognize some of these from math, they work the same way:

| **Relation**             | **Operator** |
|--------------------------|--------------|
| Equal to                 | `==`       |
| Not equal to             | `!=`       |
| Less than                | `<`       |
| Greater than             | `>`       |
| Less than or equal to    | `<=`      |
| Greater than or equal to | `>=`      |

To use these, we'll have to place two **operands**, one on either side. These work a lot like the arithmetic operators from last lesson. Just as 4 + 5 equals 9, 3 < 4 equals `true`. Here are some examples. Pay attention to what questions they ask and what they evaluate to.

| Code     | Asks this question…                             | Which evaluates to… |
|----------|-------------------------------------------------|---------------------|
| 2 == 3   | Is 2 equal to 3? No.                            | `false`           |
| 3 != 5   | Is 3 not equal to 5? Yes.                       | `true`            |
| 4 < 5   | Is 4 less than 5? Yes.                          | `true`            |
| 10 > 12 | Is 10 greater than 12? No.                      | `false`           |
| 3 <= 3  | Is 3 less than 3 or equal to 3? Yes, equal.     | `true`            |
| 4 >= 5  | Is 4 greater than 5 or equal to 5? No, neither. | `false`           |

Alright, now we have a boolean answer to a question. How do we use it?

# `if` Statements

The `if` statement allows the program to decide whether or not to execute a block of code, depending on a boolean condition. The basic structures looks like this:

```cpp
if (condition) {

}
```

If the boolean condition is `true`, the program will execute everything inside of the curly braces. If the condition isn't `true`, the program simply skips to the next line of code after the if-block (after the closing `}`).

This condition can be **anything that evaluates to a boolean**–a variable, a literal (`true` or `false`), or any of the relational operators mentioned above. The condition should be surrounded by parenthesis, and the code that is run **conditionally** needs to be enclosed inside curly braces:

```cpp
int temperature;
cin >> temperature;

if (temperature > 80) {
    cout << "It's hot outside!" << endl;
}
cout << "Program done." << endl;
```

This code lets a user input a temperature in Fahrenheit and outputs `It's hot outside` if the temperature is greater than 80 degrees. Regardless of what the temperature is, the program will always output `Program done.` This is because the second `cout` isn't part of the `if` statement's code block, so it's executed right after the `if` block is evaluated.

We can use a flowchart to visualize the **control flow** of the program. This is especially useful with more complex programs–you'll see this later

![](image1.png)

Any amount of code can be put inside an `if` block–it just needs to be enclosed in the curly braces. Also note the indentation–while it's not required by C++, it lets the programmer know what is and isn't inside the `if` block.

# `else` and `else if` clauses

## `else` clause

An `if` statement allows a program to either run or skip over a run of code. What if we wanted the program to choose between two blocks of code to run? The `else` clause can help us do that. When put after an `if` statement, the program will run the code when the condition is **not** met. Let's take our existing temperature code and output something if the temperature is **not greater than** 80:

```cpp
int temperature;
cin >> temperature;

if (temperature > 80) {
    cout << "It's hot outside!" << endl;
}
else {
    cout << "It's not hot outside!" << endl;
}
cout << "Program done." << endl;
```

The `else` clause is placed immediately after the `if` block we want to apply it to. In the code above, if the temperature is greater than 80, the condition is `false` and outputs `It's hot outside!` just like our old code did. If the temperature is less than or equal to 80, the condition becomes `false` and the code in the `else` block is run, which outputs `It's not hot outside!`.

The flowchart looks like this:

![](conditionals/image2.png)
## `else if` clauses

The `else if` clause lets us check for another condition of the preceding `if` condition is false. This lets the program make more complex decisions by testing multiple boolean conditions. Let's modify our program to also test if the temperature is below freezing:

```cpp
int temperature;
cin >> temperature;
if (temperature > 80) {
    cout << "It's hot outside!" << endl;
}
else if (temperature < 32) {
    cout << "It's freezing outside!" << endl;
}
else {
    cout << "It's neither hot nor freezing outside!" << endl;
}

cout << "Program done." << endl;
```

The program first checks if the temperature is above 80. If it is, the program outputs `It's hot outside!` and skips to `Program done.` However, if the temperature isn't above 80, the program moves onto the `else if` clause. Here, we test if the temperature is below 32–if it is, `It's freezing outside!` is outputted and we move to `Program done.`

Finally, if the temperature is neither above 80 or below 32, the program outputs `It's neither hot nor freezing outside!` and then moves to `Program done.`

The flowchart looks like this:
![](conditionals/image3.png)

The flowchart is a little complex, but the main takeaway here is that **order matters.** We're first checking if the temperature is greater than 80, then we're checking if the temperature is less than 32. This matters sometimes–consider this example:

```cpp
int temperature;
cin >> temperature;

if (temperature > 80) {
    cout << "It's hot outside!" << endl;
}

else if (temperature > 90) {
    cout << "It's really hot outside!" << endl;
}

cout << "Program done." << endl;
```

If we enter `95`, the program outputs `It's hot outside!` because the program first checks if the temperature is greater than 80. It is, so it'll print `It's hot outside!` despite the `else if` clause. If we reverse the order of the conditions, we get different behavior:

```cpp
int temperature;
cin >> temperature;

if (temperature > 90) {
    cout << "It's really hot outside!" << endl;
}
else if (temperature > 80) {
    cout << "It's hot outside!" << endl;
}
cout << "Program done." << endl;
```

Now if we enter `95`, the program outputs `It's really hot outside!` because we **first** check if the temperature is greater than 90, **then** if it isn't, we check if it's greater than 80. Usually this is what we want, so pay attention to the order of `if` clauses.

Another thing to note: in our original code, the undesired behavior only appears when we enter a number between 80 and 90. These errors can be difficult to find since we encounter a problem **only for certain inputs**.

# Nested `if` statements

