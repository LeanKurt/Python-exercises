task = []

def doneTask(task):
      exit = 0
      while not exit == 1:
        taskDone = int(input("What task number did you finish and to mark as done"))
        task[taskDone]["Done Task"] = True
        print(task[taskDone])
        ifExit = input("Do you have more task to be mark as done?").lower()  
        if ifExit == "yes" or ifExit == "y": 
           continue
        elif ifExit == "no" or ifExit == "n":  
            exit = 1
        else:
            print("You have entered an invalid input")


def addTask():
    exit = 0
    taskNo = 0  
    while not exit == 1:
        newTask = input("Add new Task: \n")
        my_task = {"Task": newTask, "Done Task": False, "taskNumber": taskNo}
        task.append(my_task)
        taskNo += 1
        print(task)
        ifExit = input("Do you want to add more Task:(yes/no) \n").lower()  # Convert input to lowercase
        if ifExit == "yes" or ifExit == "y": 
           continue
        elif ifExit == "no" or ifExit == "n":  # Use logical OR here
            exit = 1
        else:
            print("You have entered an invalid input")
        
def deleteTask(task):
    exit = 0
    taskNo = 0
    while not exit == 1:
      taskNumber = int(input("What task number do you want to remove:"))
      taskNo = taskNumber
      task.pop(taskNo)
      print(task)
      ifExit = input("Do you want to remove more Task:(yes/no) \n").lower()  # Convert input to lowercase
      if ifExit == "yes" or ifExit == "y": 
           continue
      elif ifExit == "no" or ifExit == "n":  # Use logical OR here
            exit = 1
      else:
            print("You have entered an invalid input")
            
def mainProgram(task):
    exit = 0
    while not exit == 1:
      print("Welcome to your Todo list manager in python\n")
      print("Select from the options")
      print("1. Add task")
      print("2. Delete task \n")
      print("3. Mark Task as Done")
      option = str(input("Choose a number base from your option(1-2):"))
      if option == "1":
            addTask()
      elif option == "2":
            deleteTask(task)
      elif option == "3":
            doneTask(task)
      else:
            print("Invalid option. Please select 1 or 2.")
            continue
      ifExit = input("Do you want to continue:")
      if ifExit == "yes" or ifExit == "y": 
           continue
      elif ifExit == "no" or ifExit == "n":  # Use logical OR here
            exit = 1
      else:
            print("You have entered an invalid input")

mainProgram(task)