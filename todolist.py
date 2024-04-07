#Create A TO DO List by Using Python Programming
Tasks=[]
def Show_Tasks(Tasks):
    if not Tasks:
        print("No Tasks Found")
    else:
        for i,Tasks in enumerate(Tasks):
            print((i),(Tasks))
def Add_Tasks(Tasks,new_Tasks):
    Tasks.append(new_Tasks)
    print("Tasks Added Successfully")
def Update_Tasks(Tasks,index,Update_Tasks):
    if 1 <= index <=len(Tasks):
        Tasks[index]=Update_Tasks
        print("Task updated successfully")
    else:
        print("Invalid Task index")
def Delete_Tasks(Tasks,index,Delete_Tasks):
    if Tasks:
        Delete_Tasks=Tasks.pop()
        print(f"Tasks'{Delete_Tasks}'Deleted successfully")
    else:
        print("Invalid Task index")
while True:
        print("\n To Do List ")
        print("1.Show Tasks")
        print("2.Add Tasks")
        print("3.Update Tasks")
        print("4.Delete Tasks")
        print("5.Exit")
        choice=input("Enter your Tasks(1-5): ")
        if choice =="1":
            Show_Tasks(Tasks)
        elif choice =="2":
            new_Tasks =input("Enter the Tasks to add: ")
            Add_Tasks(Tasks,new_Tasks)
        elif choice =="3":
            index=int(input("Enter the Task index to update: "))
            Update_Tasks=input("Enter the update tasks: ")
            Update_Tasks(Tasks,index,Update_Tasks)
        elif choice =="4":
            index=int(input("Enter the Task index to delete: "))
            Delete_Tasks=(Tasks,index,Delete_Tasks)
        elif choice =="5":
            print("Exiting....")
            break
        else:
            print("invalid choice:please try again..")