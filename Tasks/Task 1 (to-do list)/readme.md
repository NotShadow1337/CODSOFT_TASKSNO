# To-Do List

## Description

This is a simple command-line To-Do List application developed using Python. It helps users organize and track their daily tasks through an interactive menu.

## Features

- View Tasks
- Add Task
- Update Task
- Delete Task
- Mark Task as Completed
- Exit the Application

---

## Sample Output

### Main Menu

```text
----- TO-DO LIST -----
1. View Tasks
2. Add Task
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. Exit
```

### View Tasks (No Tasks)

```text
Enter your choice: 1

No tasks found.
```

### Add Task

```text
Enter your choice: 2
Enter task: Complete homework
Task added.
```

### View Tasks

```text
Enter your choice: 1

Tasks:
1. Complete homework (Pending)
2. Go to gym (Pending)
```

### Update Task

```text
Enter your choice: 3

1. Complete homework
2. Go to gym

Enter task number: 1
Enter new task: Complete homework and submit
Task updated.
```

### Mark Task as Completed

```text
Enter your choice: 5

1. Complete homework and submit
2. Go to gym

Enter task number: 1
Task marked as completed.
```

### Delete Task

```text
Enter your choice: 4

1. Complete homework and submit
2. Go to gym

Enter task number: 2
Task deleted.
```

### Final Task List

```text
Enter your choice: 1

Tasks:
1. Complete homework and submit (Completed)
```

### Exit

```text
Enter your choice: 6

Thank you!
```