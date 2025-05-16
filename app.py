def task_management():
    task=[]
    print("----- WELCOME TO TASK MANAGEMENT...LETS START MANAGING YOUR DAY EFFICIENTLY--------")
    total_number_of_tasks=int(input("Enter the number of task you wanna add in the list for today... = "))
    for i in range(1,total_number_of_tasks):
        task_name=input(f"Enter task {i} = ")
        task.append(task_name)
    print(f"Todays's tasks are\n{task}")
    while True:
        operation_to_perform=int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exist\Stop"))
        if operation_to_perform==1:
            add=input("Enter the task you want to perform for todays = ")
            task.append(add)
            print(f"Task {add} has been succesfully done...")
        elif operation_to_perform==2:
            update_the_value=input("Enter the task you want to update = ")
            if update_the_value in task:
                updated_value= input(" Enter the new task you want to add = ")
                ind=task.index(update_the_value)
                task[ind]=updated_value
                print(f"Update the task again {updated_value}")
        elif operation_to_perform==3:
            delete_value=input("Which task you want to delete = ")
            if delete_value in task:
                ind=task.index(delete_value)
                print(f"Task {delete_value} has been succesfully deleted")
        elif operation_to_perform==4:
            print(f"Total number of task to perform ={task}")
        elif operation_to_perform==5:
            print("Close the program if all the task for today have been decided")
            break
task_management()

