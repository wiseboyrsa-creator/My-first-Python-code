import datetime

tasks = []

def add_task():
    subject = input("Enter subject: ")
    description = input("Enter description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    assessment_type = input("Enter assessment type (e.g., Exam, Assignment, Project, Task, Test): ")
    tasks.append({
        "subject": subject,
        "description": description,
        "deadline": deadline,
        "assessment_type": assessment_type
    })
    print("✅ Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks yet!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['subject']} - {task['description']} "
                  f"(Due: {task['deadline']} | Type: {task['assessment_type']})")
        print()

def delete_task():
    if not tasks:
        print("No tasks to delete!\n")
    else:
        view_tasks()
        try:
            choice = int(input("Enter the number of the task to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"🗑️ Deleted: {removed['subject']} - {removed['description']}\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def menu():
    while True:
        print('''
📚 Hi there, how can I assist you today? 
If you need any help about your tasks, please let me know.
Here are some options to get you started:''')
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! Keep studying hard 💪")
            break
        else:
            print("Invalid choice, try again.\n")

# Run the menu
menu()
