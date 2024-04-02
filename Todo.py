task = []

def addTask():
    exit = 0
    taskNo = 0  
    while not exit == 1:
        newTask = input("Add new Task: \n")
        my_task = {"Task": newTask, "Done Task": False, "Number": taskNo}
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
      addTask()
      deleteTask(task)
      ifExit = input("Do you want to continue")
      if ifExit == "yes" or ifExit == "y": 
           continue
      elif ifExit == "no" or ifExit == "n":  # Use logical OR here
            exit = 1
      else:
            print("You have entered an invalid input")

mainProgram(task)