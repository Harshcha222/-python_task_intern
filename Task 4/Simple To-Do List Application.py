def task():
    tasks = []  # Initialize an empty list to store tasks
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    total_task = int(input("Enter how many tasks you want to add = "))
    
    # Add tasks with name, description, and completion status
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} name: ")
        task_description = input(f"Enter task {i} description: ")
        tasks.append({"name": task_name, "description": task_description, "completed": False})
    
    print("Today's tasks are:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{task['name']} - {task['description']} | Status: {status}")
    
    while True:
        try:
            operation = int(input("\nEnter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Mark as Complete\n6-Exit/Stop\n"))
            
            if operation == 1:  # Add task
                add_name = input("Enter task name to add: ")
                add_description = input("Enter task description to add: ")
                tasks.append({"name": add_name, "description": add_description, "completed": False})
                print(f"Task '{add_name}' has been successfully added.")
            
            elif operation == 2:  # Update task
                updated_val = input("Enter the task name you want to update: ")
                found = False
                for task in tasks:
                    if task["name"] == updated_val:
                        up_name = input("Enter new task name: ")
                        up_description = input("Enter new task description: ")
                        task["name"] = up_name
                        task["description"] = up_description
                        print(f"Updated task '{updated_val}' to '{up_name}'.")
                        found = True
                        break
                if not found:
                    print("Task not found.")
            
            elif operation == 3:  # Delete task
                del_val = input("Which task do you want to delete: ")
                tasks = [task for task in tasks if task["name"] != del_val]
                print(f"Task '{del_val}' has been deleted.")
            
            elif operation == 4:  # View tasks
                print("\nAll tasks:")
                for task in tasks:
                    status = "Completed" if task["completed"] else "Incomplete"
                    print(f"{task['name']} - {task['description']} | Status: {status}")
            
            elif operation == 5:  # Mark as complete
                mark_complete = input("Enter the task name to mark as complete: ")
                found = False
                for task in tasks:
                    if task["name"] == mark_complete:
                        task["completed"] = True
                        print(f"Task '{mark_complete}' marked as complete.")
                        found = True
                        break
                if not found:
                    print("Task not found.")
            
            elif operation == 6:  # Exit
                print("Closing the program....")
                break
            
            else:
                print("Invalid Input. Please enter a number from 1 to 6.")
        
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()


