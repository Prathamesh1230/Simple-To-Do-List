from task_manager import add_task, view_tasks, mark_completed, delete_task

def main():
    while True:
        print("\n🗂 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            add_task(name)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to mark as completed: "))
            mark_completed(index)

        elif choice == "4":
            view_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)

        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
