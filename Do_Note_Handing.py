
def add_task(task_id, description):
    with open("tasks.txt", 'a') as file:
        file.write(f"{task_id}|{description}|Pending\n")
    print(f"✓ Task {task_id} added!")


def view_tasks():
    with open("tasks.txt", 'r') as file:
        print("\n" + "="*50)
        for line in file:
            parts = line.strip().split('|')
            print(f"ID: {parts[0]} | {parts[1]} | {parts[2]}")
        print("="*50 + "\n")

def delete_task(task_id):
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()
    with open("tasks.txt", 'w') as file:
        for task in tasks:
            if not task.startswith(task_id + '|'):
                file.write(task)
    print(f"✓ Task {task_id} deleted!")


def mark_done(task_id):
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()
    with open("tasks.txt", 'w') as file:
        for task in tasks:
            if task.startswith(task_id + '|'):
                parts = task.strip().split('|')
                file.write(f"{parts[0]}|{parts[1]}|Completed\n")
            else:
                file.write(task)
    print(f"✓ Task {task_id} completed!")

while True:
    print("\n1. Add  2. View  3. Done  4. Delete  5. Exit")
    choice = input("Choose: ")
    
    if choice == '1':
        tid = input("Task ID: ")
        desc = input("Description: ")
        add_task(tid, desc)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        tid = input("Task ID: ")
        mark_done(tid)
    elif choice == '4':
        tid = input("Task ID: ")
        delete_task(tid)
    elif choice == '5':
        print("Bye!")
        break
    else:
        print("Invalid!")