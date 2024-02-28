tasks = []


def addTask():
    task_name = input("Enter the name of the task: ")
    tasks.append(task_name)
    print(f"\nTask '{task_name}' added successfully!")

def viewAllTasks():
    
    if tasks == False:
        print("There are no tasks available")
    else:
        print("Current Tasks:\n")
    for i, task_name in enumerate(tasks, start= 1):
        print(f"Task #{i}. {task_name}")

def deleteTask():
    if tasks == False:
        print("There is no available task to delete.")
        return
    
    viewAllTasks()
    task_index = int(input("Enter the number of the task you want to delete: ")) -1
    if task_index >= 0 and task_index < len(tasks):
        tasks.pop(task_index)
        print(f"Successfully deleted # '{tasks}'")

def updateTask():
    if tasks == False:
        print("There is no task to be updated.")
        return
    
    viewAllTasks()
    taskToUpdate = int(input("Enter the number of the task you want to update: ")) -1
    if taskToUpdate >= 0 and taskToUpdate < len(tasks):
        old_task = tasks[taskToUpdate]
        new_task = input("Enter the name of the new task: ")
        tasks[taskToUpdate] = new_task
        print(f"The task has been updated '{old_task}' to '{new_task}' successfully!.\n")
    else:
        print("Invalid index. Please try again.")


if __name__ =="__main__":
    print("Welcome to To-Do-List\n")
    while True:
        print("Please enter your choice")
        print("\t1.Add Task")
        print("\t2.View All Tasks")
        print("\t3.Delete Task")
        print("\t4.Update Task")
        print("\t5.Exit the Program")

        choice = input("Enter your desired choice: ")

        if (int(choice) == 1):
            addTask()

        elif (int(choice) == 2):
            viewAllTasks()
            
        elif (int(choice) == 3):
            deleteTask()

        elif (int(choice) == 4):
            updateTask()

        elif (int(choice) == 5):
            print("Exiting the program...\n")
            break
        else:
            print("Invalid Choice! Please try again.")

    print("Thank You for using To-Do-List")