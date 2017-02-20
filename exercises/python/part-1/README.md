# Python exercises, Part I. (basics)

## Exercise #0: Hello python!

Create a `hello.py` file with the following line as content:

```
print(``Hello python!'')
```

Run it on your own machine (`python hello.py`).


## Exercise #1a: Factorial

Ask the user for an integer `n` and compute the factorial for this number.

Hints:

  - Factorial: `0!=1`; `1!=1`; `2!=2*1=2`; `n!=n*(n-1)*(n-2)*...*1`
  - Use `int(input("Enter a number: "))` to manually input a number


## Exercise #1b: Fibonacci

Ask the use for an integer `n` and print out the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) up to that number.  E.g., if `n=10`, print out `1 1 2 3 5 8`.


## Exercise #2a: List filtering

Filter all the odd numbers from the list `[1,2,3,4,5]` and store them in a new list.


## Exercise #2b: Exam scores

The following dictionary stores four students' exam scores for a given course: `d = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74}`.
Calculate the average, max, and min scores.


## Exercise #2c: List and Dictionary operation

Similar to the previous exercise, a dictionary stores five students' scores: `e = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74, 'Dave':85}`.
Write a script that lists the name(s) of those who got 85 as score.


## Exercise #2d: Data structures

Copy the following lines and print out the values of these variables to see how these data structures work:

  - `A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))`
  - `A1 = range(10)`
  - `A2 = sorted([i for i in A1 if i in A0])`
  - `A3 = sorted([A0[s] for s in A0])`
  - `A4 = [i for i in A1 if i in A3]`
  - `A5 = {i:i*i for i in A1}`
  - `A6 = [[i,i*i] for i in A1]`


## Exercise #3a: Fibonacci function

Write a function of Fibonacci which return Fibonacci sequence up to `n`.

  - Hint: Put the scripts you have created in Exercise 1b into a function structure


## Exercise #3b: Sorting

Write a function that takes a list of numbers as parameter, and returns the list sorted.

  - Hint: use `list.sort()` or implement on your own sorting (give it a try!)


## Exercise #3c: Reverse string

Write a function that takes a string as parameter and return the reversed string. E.g., given the input `abcde` it should return `edcba`.


## Exercise #4: Read file

Write script that performs the following operations on the `my_file.txt` file:

  - Open and read this txt file
  - Print out the first line
  - Count the number of words
  - Count the number of lines


## Exercise #5a: JSON write

Make a dictionary from the following keys and values, and write that dictionary into a JSON file:

```
keys = [1,2,3,4,5]`
values = ["I", "love", "python", "very", "much"]
```


## Exercise #5b: JSON read

Read the JSON file that you generated in Exercise 5a and print all key-value pairs.


## Exercise #6: What does it do?

What does the following piece of code print? (You can run it on your machine to see the difference and understand what happens.)

```
class Parent(object):
	x = 1 class
Child1(Parent):
	pass class
Child2(Parent):
	pass
print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
```
