from models import Task
from storage import save_task, load_tasks, overwrite_tasks

def add_task(name):
    task = Task(name)
    save_task(task)
    print(f"✅ Task '{name}' added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks available.")
    else:
        print("\n📝 To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.name} [{task.status}]")

def mark_completed(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1].status = "Completed"
        overwrite_tasks(tasks)
        print(f"✅ Task '{tasks[index - 1].name}' marked as completed.")
    else:
        print("❌ Invalid index.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        overwrite_tasks(tasks)
        print(f"🗑 Task '{removed.name}' deleted.")
    else:
        print("❌ Invalid index.")
