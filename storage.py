import os
from models import Task

def save_task(task):
    with open("tasks.csv", "a") as f:
        f.write(task.to_csv())

def load_tasks():
    tasks = []
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as f:
            for line in f.readlines():
                name, status = line.strip().split(",")
                tasks.append(Task(name, status))
    return tasks

def overwrite_tasks(tasks):
    with open("tasks.csv", "w") as f:
        for task in tasks:
            f.write(task.to_csv())
