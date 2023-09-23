tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")
def update_task(task_index, new_task):
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index!")
def display_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Display tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
        task_index = int(input("Enter the index of the task to update: ")) - 1
        new_task = input("Enter the updated task: ")
        update_task(task_index, new_task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")