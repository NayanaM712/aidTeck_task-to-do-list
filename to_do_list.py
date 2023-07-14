import pickle

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description, "Not Completed")
        self.tasks.append(new_task)
        print("Task added successfully!")

    def delete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            deleted_task = self.tasks.pop(task_index)
            print(f"Deleted task: {deleted_task.title}")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found!")
        else:
            print("Current tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def update_task_status(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index!")
        else:
            task = self.tasks[task_index]
            if task.status == "Not Completed":
                task.status = "Completed"
                print(f"Task '{task.title}' status updated to 'Completed'.")
            else:
                print(f"Task '{task.title}' is already marked as 'Completed'.")

    def save_tasks(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)
        print("Tasks saved successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

def show_menu():
    print("TODO LIST APP")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Update Task Status")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Quit")

todo_list = ToDoList()

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        todo_list.add_task(title, description)
    elif choice == "2":
        task_index = int(input("Enter the index of the task to delete: "))
        todo_list.delete_task(task_index)
    elif choice == "3":
        todo_list.view_tasks()
    elif choice == "4":
        task_index = int(input("Enter the index of the task to update status: "))
        todo_list.update_task_status(task_index)
    elif choice == "5":
        filename = input("Enter the filename to save the tasks: ")
        todo_list.save_tasks(filename)
    elif choice == "6":
        filename = input("Enter the filename to load the tasks from: ")
        todo_list.load_tasks(filename)
    elif choice == "7":
        print("Thank you for using the TODO LIST APP. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
