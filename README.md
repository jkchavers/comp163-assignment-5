## Assignment 5

## Author

- Jaylen Chavers - COMP 163, Fall 2025

## Description

- This program is a series of coding challenges, demonstrating mastery of the "for" and "while" loops in Python.

## Features

- Visualization of the Collatz Conjecture sequence

- Prime number determination

- A multiplication table that goes up to 10.

## How to Run

# Python jkchavers\_assignment\_5.py

## Key choices



- I chose the while loop for the Collatz Conjecture sequence because the number of iterations could not be predetermined. User input does not factor into how many iterations occur, but the chosen number itself.

- A for loop was chosen for the prime number determination because I could use the user input to create a determined number of iterations.
- I decided to place the column loop inside of the row loop as it's easier to print formatted strings in rows than columns.







## The Collatz Conjecture Sequence Inner Workings

- The Collatz Conjecture sequence algorithm I made works by obtaining a user input, checking if it has a remainder if divided by 2. If it does divide the user input by 2 then append that number to a sequence string using +=. Else if the user input does have a remainder when divided by 2, multiply user input by 3 and add 1. In the sequential iterations the user input is modified by the previous calculations so each iteration is using a number that was created from the last.



## Prime number determination

- The algorithm used to determine a prime number was created by understanding that a prime number is a number divisible by 1 and itself. A user input and a variable with a Boolean named prime that was initialized to true were declared. I then created a for loop starting with a range function that started at 2 and ended at user input minus 1. If the user input didn't have a remainder in any number passed in from the range function, I set prime to False. Outside of the for loop an if statement was made to check if the prime Boolean was still true or if it was set to false.


## Multiplication grid

- 3 loops were used in the multiplication table challenge. I used the first loop to print the header row of numbers. Next I created an outer for loop to print the starting number of each row. Then I created a nested for loop to multiply each column number by the row numbers and then continuously print the numbers from left to right until the loop terminated at 10 iterations.





## AI Usage
### Prompt:
where is my python logic going wrong without giving me the answer? I'm trying to determine whether a given number is prime or not.        user\_number = int(input("Enter a number: "))

step_count = 0

prime = True





divisor = 2

for number in range(divisor,user\_number - 1):

   if number % divisor == 0 and divisor < user\_number:

       prime = False

       divisor += 1

      

 if prime == True:

   print(user\_number," is prime!")

 elif prime == False:

  print(user\_number,"is not prime (divisible 3)")

   
### ChatGPT response:
 Absolutely — let's walk through the logic without giving away the fix.



 You're trying to determine whether a number is prime by checking its divisibility. Here's how you can debug this on your own:



1\. \*\*Loop Range\*\*: Look at what numbers you're iterating over in the `for` loop. Are they the correct candidates to check for factors of `user\_number`?



2\. \*\*Divisibility Check\*\*: Examine your `if` condition — who is being divided by whom? Is this condition actually testing whether `user\_number` is divisible by the current number?

 

3\. \*\*Divisor Increment\*\*: You're modifying `divisor` inside the loop — is that the correct variable to increment? How does this affect the logic of your `for` loop, and is it even necessary?



4\. \*\*Loop Exit and Final Check\*\*: Think about when your loop will stop and whether it catches all possible non-prime cases. Does it terminate early if a factor is found?

 

5\. \*\*Error Message Content\*\*: Your `print()` for the non-prime case includes `"divisible 3"` — is that hardcoded, and if so, does that reflect the actual divisor?



Try tracing your program with `user\_number = 9` or `user\_number = 5` and print out key variables during each iteration to see what’s actually being tested.



Let me know what you find!



