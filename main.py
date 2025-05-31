list_task = []

def add_task():
    """
    Adds a new task to the to-do list with a default status of 'Pending'.
    Prompts the user to enter the task description.
    """
    new_task = input("Enter a new task: ")
    list_task.append({"task": new_task, "status": "Pending"})
    print("Task Added\n")

def view_task():
    """
    Displays all tasks in the to-do list along with their status.
    If there are no tasks, informs the user.
    """
    if len(list_task) == 0:
        print("No Task added")
    else:
        print("Current Task: \n")
        for i, task in enumerate(list_task, 1):
            print(f"{i}. {task['task']} - {task['status']} ")
        print("\n")

def remove_task():
    """
    Removes a task from the to-do list based on user selection.
    Shows the list of tasks and asks the user to choose which one to remove.
    Handles invalid input gracefully.
    """
    if len(list_task) == 0:
        print("No Task added")
    else:
        try:
            view_task()
            remove_task = int(input("ENTER the Task to be removed: ")) - 1
            if 0 <= remove_task < len(list_task):
                removed = list_task.pop(remove_task)
                print(f"\n Task Removed: {removed['task']} \n")
                view_task()
            else:
                print("\n Invalid Task Number")
        except ValueError:
            print("\n Please enter a valid number")

def doing_task():
    """
    Changes the status of a selected task to 'Doing'.
    Prompts the user to select which task is being worked on.
    Handles invalid input.
    """
    if len(list_task) == 0:
        print("No Task added")
    else:
        try:
            view_task()
            doing_task = int(input("Enter the Task that you are doing: ")) - 1
            if 0 <= doing_task < len(list_task):
                list_task[doing_task]['status'] = 'Doing'
                print(f"\n Status Changed for : {list_task[doing_task]['task']} -  Doing  \n")
            else:
                print("\n Invalid Task Number")
        except ValueError:
            print("\n Please enter a valid number")

def done_task():
    """
    Marks a selected task as 'Completed'.
    Prompts the user to select which task is finished.
    Handles invalid input.
    """
    if len(list_task) == 0:
        print('No Task Added')
    else:
        view_task()
        try:
            done_task = int(input('Enter Task that is Completed: ')) - 1
            if 0 <= done_task < len(list_task):
                list_task[done_task]['status'] = 'Completed'
                print(f"\n Task: {list_task[done_task]['task']} is Completed")
            else:
                print("\n Invalid Task Number")
        except ValueError:
            print("\n Please enter a valid number")

def menu():
    """
    Displays the main menu for the to-do list application and handles user choices.
    Allows the user to add, view, remove, update, or complete tasks, or exit the application.
    """
    while(True):
        print("\n \n ***Welcome to the To-Do List Application****\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Doing")
        print("5. Marked as done")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            doing_task()
        elif choice == "5":
            done_task()
        elif choice == "6":
            print("Exiting the application")
            exit()
        else:
            print("Invalid Response")

menu()
