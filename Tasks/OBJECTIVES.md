# Task Objectives and Learnings

This file contains the objectives, concepts learned, and important code explanations for each task completed during the Python Internship.

---

# Task 1 - To-Do List

## Objective

Create a simple To-Do List application that allows users to add, view, update, delete, and complete their tasks.

## Concepts Learned

- Lists
- Loops
- Conditional statements
- User input handling
- Data storage using lists

## Important Code

### Creating the task list

```python
tasks = []
```

Creates an empty list to store all the tasks.

---

### Adding a task

```python
tasks.append([task, False])
```

Adds a new task to the list along with its completion status.

`False` represents that the task is not completed.

---

### Running the menu continuously

```python
while True:
```

Keeps the program running until the user selects the exit option.

---

# Task 2 - Calculator

## Objective

Create a simple calculator that performs basic arithmetic operations like addition, subtraction, multiplication, and division.

## Concepts Learned

- Arithmetic operators
- Conditional statements
- User input
- Menu-driven programs

## Important Code

### Taking user choice

```python
choice = input("Enter your choice: ")
```

Stores the operation selected by the user.

---

### Performing calculations

```python
if choice == "1":
```

Checks which operation the user selected and performs the required calculation.

---

### Division by zero handling

```python
if num2 == 0:
```

Prevents the program from dividing a number by zero.

---

# Task 3 - Password Generator

## Objective

Create a program that generates a random password based on the length entered by the user.

## Concepts Learned

- Random values
- Strings
- Loops
- User input

## Important Code

### Importing required modules

```python
import random
import string
```

`random` is used to select random characters and `string` provides letters, numbers, and symbols.

---

### Creating character options

```python
characters = string.ascii_letters + string.digits + string.punctuation
```

Creates a collection of characters that can be used in the password.

---

### Generating password

```python
password = password + random.choice(characters)
```

Selects a random character and adds it to the password.

---

# Overall Learning

Through these tasks, I learned the basics of Python programming including:

- Variables
- Lists
- Loops
- Conditions
- User input
- Random module
- Data handling
- Building simple command-line applications
