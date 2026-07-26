tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks found.")
        else:
            print("\nTasks:")
            i = 1
            for task in tasks:
                if task[1] == True:
                    print(str(i) + ". " + task[0] + " (Completed)")
                else:
                    print(str(i) + ". " + task[0] + " (Pending)")
                i = i + 1

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append([task, False])
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            i = 1
            for task in tasks:
                print(str(i) + ". " + task[0])
                i = i + 1

            num = int(input("Enter task number: "))

            if num >= 1 and num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1][0] = new_task
                print("Task updated.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            i = 1
            for task in tasks:
                print(str(i) + ". " + task[0])
                i = i + 1

            num = int(input("Enter task number: "))

            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            i = 1
            for task in tasks:
                print(str(i) + ". " + task[0])
                i = i + 1

            num = int(input("Enter task number: "))

            if num >= 1 and num <= len(tasks):
                tasks[num - 1][1] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")