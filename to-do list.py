todo_list = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f'"{task}" added to the list.')

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f'"{removed}" removed from the list.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")



