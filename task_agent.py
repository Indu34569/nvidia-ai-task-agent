from datetime import datetime

def save_task(task):
    with open("task_history.txt", "a") as file:
        file.write(f"{datetime.now()}: {task}\n")

def show_history():
    print("\nPrevious tasks:")
    try:
        with open("task_history.txt", "r") as file:
            for line in file:
                print("-", line.strip())
    except FileNotFoundError:
        print("No previous tasks yet.")

while True:
    task = input("\nWhat do you need help with? ").strip()

    if task.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if "study" in task.lower() or "learn" in task.lower() or "hackathon" in task.lower():
        print("\nStudy plan:")
        print("1. Define what you need to learn.")
        print("2. Study for 30 minutes.")
        print("3. Take a 10-minute break.")
        print("4. Practice for 30 minutes.")
        print("5. Review what you learned.")

    elif "email" in task.lower() or "message" in task.lower():
        print("\nEmail plan:")
        print("1. State the purpose.")
        print("2. Add the important details.")
        print("3. Make the request clear.")
        print("4. Finish politely.")

    elif "history" in task.lower() or "previous" in task.lower():
        show_history()

    else:
        print("\nI don't have a special workflow for that yet.")
        print("First step: break the task into one small action.")

    save_task(task)
