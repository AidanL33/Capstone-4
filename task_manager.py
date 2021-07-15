#libraries
from datetime import date
from datetime import datetime


        #=====global variables=====
user_info = {}


        #=====difining functions=====
def reg_user():
       
    if user_username != "admin":
        print("Only the username with 'admin' can request this option!") 

    #only admin username will have the option to register a new users
    elif user_username == "admin": #The following menu will show when admin is logged in
        new_user = input("Please enter a new username:\n")
    
#while loop  and if statement to check if username is correct
        while new_user in user_info:
            print("Username already exist try again!\n")
            new_user = input("Enter a valid username:\n")

        new_user_password = input("Please enter a new password:\n")

        new_password = False

    #while loop and an if/elif statement to confirm the new password thats been entered 
        while new_password == False:
            confirm_new_password = input("Please confirm password:\n")

            if new_user_password == confirm_new_password:
                new_password = True
            print("New username and password is saved!")    

            if new_password == False:
                print("Your password does not match")

        with open("user.txt", "a") as file:
            file.write(f"\n{new_user}, {new_user_password}") #write() function to write the new username and password to the file

def add_task():
    task_file = open("tasks.txt", "a+") #opening the file tasks.txt to add new tasks 

    new_task_username = input("Please enter the username to whom the task is assigned to:\n")
    new_task_title = input("Please enter the title of the task:\n")
    new_task_description = input("Please add the description of the task:\n")
    new_task_assigned_date = input("Please enter the date the task was assigned:\n")
    new_task_due_date = date.today()
    new_task_completed = input("Is the task completed (Yes / No):\n")

    task_file.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {new_task_due_date}, {new_task_assigned_date},  {new_task_completed}")

    task_file.close()

def view_all():
    task_file = open("tasks.txt", "r") #opening the file tasks.txt to view all the tasks

    for info in task_file:
        new_task_username, new_task_title, new_task_description, new_task_assigned_date, new_task_due_date, new_task_completed = info.split(", ")

        print(f'''
        New task username:\t{new_task_username}
        Task title:\t\t{new_task_title}
        Task desciption:\t{new_task_description}
        Task assigned date:\t{new_task_assigned_date}
        Task due date:\t\t{new_task_due_date}
        Task completion:\t{new_task_completed}
        ''')

    task_file.close()

def view_mine():
    view_tasks = open("tasks.txt", 'r')#opening the file tasks.txt to view all my tasks
    task_number = 1 #making task_number variable = 1
    task_dictionary = {} #creating an empty dictionary
    
    for info in view_tasks:
        new_task_username, new_task_title, new_task_description, new_task_assigned_date, new_task_due_date, new_task_completed = info.split(", ")
        task_dictionary[task_number] =  info.strip('\n').split(", ")
        if user_username == new_task_username:
            print(f'''
        Task Number:\t{task_number}
        New task username:\t{new_task_username}
        Task title:\t{new_task_title}
        Task desciption:\t{new_task_description}
        Task assigned date:\t{new_task_assigned_date}
        Task due date:\t{new_task_due_date}
        Task completion:\t{new_task_completed}
        ''')
        task_number += 1

    view_tasks.close()

    task_choice = int(input('Select task by entering task number or -1 to exit: ')) #asking user to mark or edit a task

    #making a new menu to either edit a task or mark a task
    selected_task = task_dictionary[task_choice]
    task_menu = input('''​select the following options: 
    m - mark the task as complete 
    et - ​edit the task\n''')

    #if/elif statement to mark a task complete and choose the edit option
    if task_menu == 'm':
        selected_task[-1] = 'Yes'

    elif task_menu == 'et':
        edit_choice = input('''Select the following options:
        u - edit username
        dd - edit due date\n''') #edit menu to edit username or due date

        #if user chooses 'u' they will edit the username of the task
        if edit_choice == 'u':
            edit_user = input("Please enter a new username:\n")
            selected_task[0] = edit_user
        #if user chooses 'dd' they will edit the due date of the task
        elif edit_choice == 'dd':
            edit_date = input("Please enter a new due date:\n")
            selected_task[-2] = edit_date

    task_dictionary[task_choice] = selected_task
    datafile = [', '.join(tsklist) for tsklist in task_dictionary.values()]
    tofile = '\n'.join(datafile)
    print(tofile)

def task_overview():
    view_tasks = open("tasks.txt", 'r') #opening the file tasks.txt to view all my tasks
    total_numb_task = 0 #setting total number of tasks to zero 
    total_compTask = 0 #setting total number of completed tasks to zero
    total_incompTask = 0 #setting total number of incomplete tasks to zero
    total_incompleted_tasks_overDue = 0 #setting total of tasks that are incomplete and overdue zero
    percent_of_tasks_overDue = 0 #setting percentage of tasks over due to zero

    for info in view_tasks:
        new_task_completed = info.strip('\n').split(", ")[-1]
        total_numb_task += 1 #adding 1 to the variable that is storing total number of task
        
        # if/else statement to find how many tasks are completed and incomplete
        if new_task_completed.lower() == "yes":
            total_compTask += 1 #adding 1 to the variable that is storing total completed tasks
        else:
            total_incompTask += 1 #adding 1 to the variable that is storing the total of incompleted tasks
            
            strDate = info.split(", ")[-2].strip()
            date_time_obj = datetime.strptime(strDate, '%d %b %Y')

            currentdate = datetime.now()

            if date_time_obj < currentdate:
                total_incompleted_tasks_overDue += 1


     #this is to calculate the percentage of incompleted tasks
    percentage_incomplete_tasks = (total_incompTask / total_numb_task) * 100
    percentage_tasks_overdue = (total_incompleted_tasks_overDue / total_numb_task) * 100
    
    view_tasks.close()

    toverview = open('task_overview.txt', 'w') #opening a new file called task_overview.txt and writing all the data below into the file
    toverview.write(f"The total number of task is: {total_numb_task}\n")
    toverview.write(f"The total number of completed tasks is: {total_compTask}\n")
    toverview.write(f"The total number of incompleted tasks: {total_incompTask}\n")
    toverview.write(f"The total number of tasks that haven’t been completed and that are overdue: {total_incompleted_tasks_overDue}\n")
    toverview.write(f"The percentage of tasks that are incomplete: {percentage_incomplete_tasks} %\n")
    toverview.write(f"The percentage of tasks that are overdue: {percentage_tasks_overdue} %")

#function for user data and task data
def eachuser(userName, totalNumberTask):
    view_tasks = open("tasks.txt", 'r') #opening the file tasks.txt to view all my tasks
    total_tasks_assigned_to_user = 0

    total_uncompleted = 0
    total_completed = 0

    percentage_of_tasks_completed_by_user = 0
    percentage_of_tasks_incomplete_by_user = 0
    percentage_of_tasks_incomplete_overdue_by_user = 0
    percent_of_task_assinged = 0
    percent_task_overdue_by_user = 0
    #The variables above are to store the percentages and are all set to 0

    #for loop to read the username and if the task is marked yes
    for info in view_tasks:
        file_user = info.strip('\n').split(", ")[0]
        comp_task = info.strip('\n').split(", ")[-1]

        #this if statement is to see which task is assigned to which user
        if file_user == userName:
            total_tasks_assigned_to_user += 1
    
            #this if/eles statement works out in the task is completed or not
            if comp_task.lower().strip() == "yes":
                total_completed += 1
            else:
                total_uncompleted += 1

                #this is to find out id the date is overdue
                strDate = info.split(", ")[-2].strip()
            date_time_obj = datetime.strptime(strDate, '%d %b %Y')

            currentdate = datetime.now()

            if date_time_obj < currentdate:
                percentage_of_tasks_incomplete_overdue_by_user += 1
    
    #the percentage of tasks assigned to user
    percent_of_task_assinged = (total_tasks_assigned_to_user / totalNumberTask) * 100

    if total_tasks_assigned_to_user > 0:
        percentage_of_tasks_completed_by_user = (total_completed / total_tasks_assigned_to_user) * 100
        percentage_of_tasks_incomplete_by_user = (total_uncompleted / total_tasks_assigned_to_user) * 100
        percent_task_overdue_by_user = (percentage_of_tasks_incomplete_overdue_by_user / total_tasks_assigned_to_user) * 100

    #all the data that shows in the user_overview file
    userdetails = (f"details for user {userName}")
    userdetails += (f"\nTotal number of tasks assigned to user:{total_tasks_assigned_to_user}")
    userdetails += (f"\npercentage of tasks assigned to user: {percent_of_task_assinged} %")
    userdetails +=(f"\nPercent of tasks completed by user: {percentage_of_tasks_completed_by_user} %")
    userdetails += (f"\npercentage of tasks incompleted by user: {percentage_of_tasks_incomplete_by_user} %")
    userdetails += (f"percentage of tasks overdue and incomplete by user: {percent_task_overdue_by_user} %")
    return userdetails


def user_overview():
    view_users = open("user.txt", "r")
    task_file = open('tasks.txt','r')

    total_users_reg = 0 #setting the total number of users to 0
    total_num_task = len(task_file.readlines())

    usernamesList = [] #username list
    for use in view_users:
        usernamesList.append(use.split(', ')[0].strip()) 
        total_users_reg +=1 #counting the number of users

    #this is to sum up to total of the tasks and all the users
    userdata = (f"Total number of users: {total_users_reg}\n")
    userdata = (f"Total number of tasks: {total_num_task}")
    for u in usernamesList:
        userdata += '\n'+ eachuser(u, total_num_task)

    #closes both of the user.txt file and task.txt file
    view_users.close()
    task_file.close()

    uoverview = open("user_overview.txt", "w") #opening user_overview.txt file to w all the data into the file
    uoverview.write(userdata)

#calling the file functions
def generate_reports():
    task_overview()
    user_overview()

#display stats functions
def display_stats():
    print("Stats of the Task file:\n")
    dis_task = open("task_overview.txt", "r")
    print(dis_task.read())

    dis_task.close()

    print("Stats of the User file:\n")
    dis_users = open("user_overview.txt", "r")
    print(dis_users.read())

    dis_users.close()
    #all the above is to open the task_overview file and user_overview file
    #and to print the data onto the console

        #=====main program=====

#opening user.txt to read username in file
with open("user.txt", "rt") as username:
    for line in username:
        username, password = line.split(", ")
        user_info[username.strip()] = password.strip() #strip to remove the whitespaces
    
user_username = input("Enter username here:\n") #asking user to enter the username: (admin)
    
#while loop  adn if statement to check if username is correct
while user_username not in user_info:
    print("Username incorrect!\n")
    user_username = input("Enter a valid username:\n")

if user_username in user_info:
    print("Username correct!\n")

user_password = input("Enter your password:\n") #asking user to enter password

#while loop and if statement to check if the password is correct
while user_password != user_info[user_username]:
    print("Invaled password\n")
    user_password = input("Enter the correct password:\n")

if user_password != user_info[user_username]:
    print("Your password is correct\n")

if user_username == 'admin':
        userchoice = input('''Please select one of the following options: 
        r - register user:
        a - add task:
        va - view all tasks:
        vm - view my task:
        gr - generate reports:
        ds - display statistics:
        e - exit
        ''')
else:
#user chooses which option to go into
    userchoice = input('''Please select one of the following options:
    r - register user:
    a - add task:
    va - view all tasks:
    vm - view my task:
    e - exit\n''')


    #=====Calling the functions=====  

# register new user and save new username and password to the file user.txt
if userchoice == 'r':
    reg_user()

#add task in an elif statement and save it to the file tasks.txt
elif userchoice == 'a':
    add_task()

#view all tasks in an elif statement in the file tasks.txt
elif userchoice == 'va':
    view_all()

#view my tasks in an elif statement in the file tasks.txt
elif userchoice == 'vm':
    view_mine()

#elif statement if the option 'd' is chosen
elif userchoice == 'gr':
    generate_reports()

#elif statement if the option 'ds' is chosen
elif userchoice == 'ds':
    display_stats()
