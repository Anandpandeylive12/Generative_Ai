What Are Comprehensions in Python?

Comprehensions in Python are a compact, readable, and efficient way to create new sequences (like lists, sets, or dictionaries) from existing ones — all in a single line of code.

They are basically shortcuts for loops that build new collections.

** Why Use Comprehensions?

Because they:

Make code shorter

Are easier to read

Often run faster than traditional loops

Types of Comprehensions

Python supports four types of comprehensions:

Type	Syntax Example	Returns
List Comprehension	[x for x in range(5)]	List
Set Comprehension	{x for x in range(5)}	Set
Dictionary Comprehension	{x: x**2 for x in range(5)}	Dictionary
Generator Expression	(x for x in range(5))	Generator (iterator)

 1. List Comprehension

Used to create a list in one line.

Example:
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)


 Output:

[1, 4, 9, 16, 25]

With a condition:
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


 Output:

[2, 4]

 2. Set Comprehension

Creates a set (no duplicates).

nums = [1, 2, 2, 3, 3, 4]
unique_squares = {n**2 for n in nums}
print(unique_squares)


Output:

{16, 1, 4, 9}

3. Dictionary Comprehension

Used to build dictionaries quickly.

squares = {n: n**2 for n in range(5)}
print(squares)

 Output:

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

 4. Generator Expression

Same idea — but uses parentheses () instead of brackets [], and does not store the entire result in memory.

gen = (n**2 for n in range(5))
for val in gen:
    print(val)


 Output:

0
1
4
9
16

 In Simple Terms
Without comprehension	With comprehension
```python	
result = []	
for i in range(5):	
result.append(i*i)


|python
result = [i*i for i in range(5)]


Both do the same thing — but the second is shorter, cleaner, and more “Pythonic.” 

---

Would you like me to show a few **real-world exam