import sqlite3
connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
task_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT,
due_date DATE, 
status TEXT DEFAULT 'pending'
)
''')
connection.commit()
def add_task(title, description, due_date):
    cursor.execute('''
    INSERT INTO tasks (title, description, due_date)
    VALUES(?, ?, ?)
    ''', (title, description, due_date))
    connection.commit()

add_task(
    title=input("What is the name of the task?"),
    description=input("Describe The task?"),
    due_date=input("When do you want to complete the task?"),
)
def receive_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found.")
    else:
        all_completed = True
        pending_tasks = []

        for task in tasks:
            if task[4] != 'completed':
                all_completed = False
                pending_tasks.append(task)
        if not all_completed:
            for task in pending_tasks:
                print(f"ID: {task[0]}, Title: {task[1]}")
            return pending_tasks
        else:
            print("all tasks are completed")
            return[]

See_list = input("Do you want to see your current to do list? Yes or No")
print(See_list)
if See_list == "Yes":
    pending_tasks = receive_tasks()
Change_list = bool(input("Are any of these tasks completed?"))
while Change_list == True:
    list_change = input("What is the name of the completed task?")
    for task in pending_tasks:
        if list_change == task[1]:
            cursor.execute("UPDATE tasks SET status = 'completed' WHERE task_id = ?", (task[0],))
            connection.commit()
            print(f"Task '{task[1]}' marked as completed.")













