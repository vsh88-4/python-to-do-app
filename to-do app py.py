import matplotlib.pyplot as plt
def to_do_list():
    tasks = []
    completed=0

    while True:
        print("\n To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Productivity tracker ")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if tasks:
                print("Your tasks: ")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added yet. ")

        elif choice == "2":
            task = input("Enter a task: ").strip()
            tasks.append(task)
            print(f"{task} has been added to the list")

        elif choice == "3":
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                completed += 1
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number. ")

        elif choice == "4":
            total=len(tasks)+completed
            if total>0:
                productivity=(completed/total)*100
                print(f"Productivity: {productivity:.2f}%")
                pending=len(tasks)
                labels=['Completed','Pending']
                values=[completed, pending]
                plt.pie(values, labels=labels, autopct='%1.1f%%')
                plt.title("Task Productivity")
                plt.show()
            else:
                print("No tasks yet.")
        
        elif choice=="5":
            print("Goodbye!")
            break


        else:
            print("Invalid option")

to_do_list()