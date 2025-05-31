# To-Do-List-Basic
## Overview

This is a simple command-line To-Do List application written in Python. It allows users to add, view, remove, and update the status of tasks.

## Features

- **Add Task**: Add a new task with a default status of "Pending".
- **View Tasks**: Display all tasks with their current status.
- **Remove Task**: Delete a task by selecting its number.
- **Mark as Doing**: Update a task's status to "Doing".
- **Mark as Done**: Mark a task as "Completed".
- **Menu System**: User-friendly menu for navigation.

## How It Works

1. **Task Storage**  
    All tasks are stored in a list called `list_task`, where each task is a dictionary with `task` (description) and `status` (Pending/Doing/Completed).

2. **Functions Explained**

    - `add_task()`:  
      Prompts the user to enter a new task description and adds it to the list with a status of "Pending".

    - `view_task()`:  
      Lists all current tasks with their status. If there are no tasks, it notifies the user.

    - `remove_task()`:  
      Shows the list of tasks and asks the user to select one to remove. Handles invalid input gracefully.

    - `doing_task()`:  
      Lets the user select a task to mark as "Doing". Handles invalid input.

    - `done_task()`:  
      Lets the user select a task to mark as "Completed". Handles invalid input.

    - `menu()`:  
      Displays the main menu, takes user input, and calls the appropriate function based on the user's choice. The loop continues until the user chooses to exit.

3. **Running the Application**

    Run the script. The menu will appear in the terminal. Enter the number corresponding to the action you want to perform.

## Example Usage

```
***Welcome to the To-Do List Application****

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Task as Doing
5. Marked as done
6. Exit

Enter your choice: 1
Enter a new task: Buy groceries
Task Added
```

## Requirements

- Python 3.12

## License

This project is open source and free to use.


