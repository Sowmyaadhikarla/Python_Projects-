import json
import os
Filename = "tasks.js"
tasks=[]

if os.path.exists(Filename):
    with open(Filename,"r")as f:
        tasks=json.load(f)
        
def save():
    with open(Filename,"w")as f:
        json.dump(tasks,f)
        
def add_task(task_name):
    tasks.append({"task":task_name,"done":False})
    save()
    print(f"Task added:{task_name}")
    
def view():
    if not tasks:
        print("No task yet!")
    for i, t in enumerate(tasks,start=1):
        status="✔️"if t['done'] else "❌"
        print(f"{i}.{t['task']} [{status}]")
        
def mark_done(index):
    if 0<=index<len(tasks):
        tasks[index]['done']=True
        save()
        print(f"task'{tasks[index]['task']}' completed")
    else:
        print("Invalid task number!")
        
def delete_task(index):
    if 0<=index<len(tasks):
        removed=tasks.pop(index)
        save()
        print(f"Task removed:{removed['task']}")
    else:
        print("invalid task number!")

def edit_task(index,new_name):
    if 0<=index<len(tasks):
        old_name=tasks[index]["task"]
        tasks[index]['task']=new_name
        save()
        print(f"Task updated '{old_name}'->'{new_name}'")
    else:
        print("You entered an invalid input!")
        
while True:
    print("\n---To Do List---")
    print("1.Add Task")
    print("2.View Task")
    print("3.Mark Done")
    print("4.Delete Task")
    print('5.Exit')
    
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Enter a valid input")
        continue
    
    if choice==1:
        task_name=input("enter task:")
        add_task(task_name)
    elif choice==2:
        view()
    elif choice==3:
        view()
        try:
            index=int(input("Enter index of task to mark as done:"))-1
        except ValueError:
            print("Enter a valid input")
            continue
        mark_done(index)
    elif choice==4:
        view()
        index=int(input("Enter index of task to be delete:"))-1
        delete_task(index)
    elif choice==5:
        view()
        index=int(input("Enter index to be edit:"))-1
        new_name=input("Enter new name:")
        edit_task(index,new_name)
    elif choice==6:
        print("Byeee...")
        break
    else:
        print( "You enterd an invalid choice:")
        