import json
import webbrowser


#To do list application
lists = {}
def menu():
    print("\n To-Do List Menu:")    
    print('---------------------------------')
    print('1 : Create a new List')
    print('---------------------------------')
    print('2: Add a task to the list')
    print('---------------------------------')
    print('3: View List')
    print('---------------------------------')
    print('4: Delete Task')
    print('---------------------------------')
    print('5: Save List')
    print('---------------------------------')
    print('6: Exit')
    choices = input('Enter choice: ')
    if choices not in ['1','2','3','4','5','6']:
        print('Invalid choice')
        return
    else:
        return choices


def create_list():
    list_name = input('Enter the name of the list: ')
    append_list = []
    if list_name == '':
        print('List name cannot be empty')
        return
    elif list_name in lists:
        print('List already exists')
        return
    else:
        lists[list_name] = append_list
        print('List created successfully')
        return list_name, append_list
    
def add_task(list_name, append_list):
    list_name = input('Enter the name of the list to add a task: ')
    if list_name in lists:
        task = input('Enter the task to add: ')
        if task == '':
            print('Task cannot be empty')
        else:
            lists[list_name].append(task)
            print('Task added successfully')
    else:
        print('List does not exist')
        
        
        
        
        
###################################################
def view_list(list_name, append_list):
   list_name = input('Enter the name of the list to add a task: ')
   if list_name 
###################################################






def delete_task(list_name, append_list):
    view_list(list_name, append_list)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(append_list):
       task = append_list.pop(task_number-1)
       print(f"Task '{task}' deleted successfully")
    else:
        print('Invalid task number')
        return

def save_list():
    list_name = input('Enter the name of the list you want to save')
    if list_name in lists:
        openfile = open('list.txt', 'w')
        openfile.write(list_name)
        openfile.close()
        print('List saved successfully')
    else:
        print('List name cannot be empty')
        return

def open_website(url):
    webbrowser.open(url)

def main():
    while True:
        choice = menu()
        if choice == '1':
            create_list()
        elif choice == '2' :
            add_task()
        elif choice == '3':
            view_list()
        elif choice == '4': 
            delete_task()
        elif choice == '5':
            save_list()
        elif choice == '6':
            open_website("http://www.yourwebsite.com")  # Replace with your URL
            break

if __name__ == '__main__':
    app = main()