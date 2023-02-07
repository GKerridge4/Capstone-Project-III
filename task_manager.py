# =====*** TASK MANAGER PROJECT ***=====
# ===== IMPORTING LIBRARIES =====

from datetime import date
from datetime import datetime


# ===== DICTIONARIES =====

dict_usernames = {}     # This is a dictionary loop to collect data from user.txt
with open("user.txt") as user:
    for line in user:
        # Split the information into a list of
        # 'username: password'
        key, val = line.split(', ')
        # Strip '\n' from the data
        val = val.strip('\n')
        dict_usernames[key] = val
    for line in user:
        # Split the information into a list of
        # 'username: password'
        key, val = line.split(', ')
        # Strip '\n' from the data
        val = val.strip('\n')
        dict_usernames[key] = val


# ===== FUNCTIONS =====
# Current User Variable:
def username():         # User enters username. Code checks if correct.
    while True:
        current_username = input("Username: ").lower()
        
        # Making sure the user enters the correct details.
        if current_username in dict_usernames:
            print('Success!')
            break 
        else:
            print('Incorrect username')
    return current_username
current_username = username()
def user_password():    # User enters password. Code checks if correct.
    while True:
        password = input("Password: ").lower()
        
        # Making sure the user enters the correct details.
        if password == dict_usernames[current_username]:
            print('Success!')
            break
        else:
            print('Password incorrect')
    return password
password = user_password()

def user_menu():        # Shows menu to user and asks for an input.
   
    # Present the menu to the user dependent on admin or other.
    while True: 
    
    # Menu displayed for admin:
        if current_username == 'admin':      
            menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my tasks
    gr - Generate reports
    vr - View reports
    ds - Display statistics
    e - Exit
    : ''').lower()
            if menu == 'r': 
                reg_user()
            elif menu == 'a':
                add_task()
            elif menu == 'va':
                view_all()
            elif menu == 'vm':
                view_mine()
            elif menu == 'gr':
                gen_rep()
            elif menu == 'vr':
                view_rep()
            elif menu == 'ds':
                display()
            elif menu == 'e':
                exit_menu()
        elif current_username != 'admin':     
    
    # Menu displayed for all other users:
            menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my tasks
    e - Exit
    : ''').lower()
            if menu == 'r': 
                reg_user()
            elif menu == 'a':
                add_task()
            elif menu == 'va':
                view_all()
            elif menu == 'vm':
                view_mine()
            elif menu == 'e':
                exit_menu()
        else:   
            # If incorrect input, user will be promted to try again.
            print("You have made a wrong choice, Please Try again")
def getPercent(first, second, integer = False):
    '''
    :param first: (int or float) The number you would like to divide.
    :param second: (int or float) The nuber you would like to divide by.
    :param integer: (Boolean) Rounds your result to the nearest whole number.
    :return: The percentage of your first number in relation to your second.
    '''
    percent = first / second * 100
   
    if integer:
        return int(percent)
    return percent

# ===== MENU FUNCTIONS =====

def reg_user():     #'r' Registering a New User 
   
    # The user wants to add a new user to the file.
    # To make sure they enter the right username & password
    # the user will be asked to enter both twice.
    
    if current_username == 'admin':
        while True:
            new_username = input("\nPlease enter a new username: ")
            if new_username in dict_usernames:
                print("This user already exists, please try a different username.")
                while True:
                    return_to_menu = input("Would you like to return to the menu? (Yes or No) ")
                    if return_to_menu.lower() == 'yes':
                        user_menu()
                    elif return_to_menu.lower() == 'no':
                        break
                    else:
                        print("Please enter 'Yes' or 'No'.")
                    continue
            elif new_username not in dict_usernames:
                while True:
                    check_username = input("Please enter new username again: ")
                    if new_username == check_username:
                        break
                    elif new_username != check_username:
                        print(f"They don't seem to match.\nYou entered {new_username}.")
                        # Runs a double check as it seems the user is unsure of their entry.
                        # Also, showing the original user entry so they can 
                        # check without scrolling through the terminal.
                        double_check_username = input("Is this the new user you want to enter? (Yes/No): ").lower()
                        while True:
                            if double_check_username == 'yes':
                                break
                            elif double_check_username == 'no':
                                return
                            else:
                                double_check_username = input("Please enter 'Yes' or 'No')").lower()
                    else:
                        print("They don't seem to match, try them both again.\n")
                while True:
                    new_password = input("Please enter a new password: ")
                    check_password = input("Please enter new password again: ")
                    if new_password == check_password:
                        break
                    else:
                        print("They don't seem to match, try them both again.\n")
                with open('user.txt', 'a') as user:
                    user.write(f"\n{new_username}, {new_password}")
                    print("\n*** New username added to file. ***\n")
                    break
    elif current_username != 'admin':
        print('\n*** Only the admin can register a new user. ***\n')
def add_task():     #'a' Adding a Task  
        
    # The user would like to add a new task.
    # To make sure the user is adding said task
    # to an existing user we must run check of the input.
    # Then the user will be asked to enter the
    # rest of the task information.

    while True:
        task_person = input("\nWho would you like to assign the new task to? ")
        with open('user.txt') as user:
            for line in user:
                # Split the information into a list of
                # 'username: password'
                key, val = line.split(', ')
                # Strip '\n' from the data
                val = val.strip('\n')
                dict_usernames[key] = key
    
        if task_person in dict_usernames:    
            task_file = open('tasks.txt', 'a')
            task_file.write(f"\n{task_person}, ")
            task_file.close()
            break
        else:
            print('User not in list.\nPlease add user first or try again.')

    # Now the user must enter task information.
    task_title = input("What is the title of this task? ")
    task_desc = input("What is the description of this task? ")
    
    # By using map and datetime we can format the users input to match.
    task_due_date = input("What is the due date of this task? (Format: 2020,02,22) ")
    year, month, day = map(int, task_due_date.split(','))
    TDD_formated = datetime(year, month, day).strftime("%d %b %Y")
    
    # Import todays date from the 'date' module
    date_today = date.today().strftime("%d %b %Y")
    task_complete = 'No'
    
    # Append the users input into tasks.txt file
    tasks = open('tasks.txt', 'a')
    tasks.write(f"{task_title}, {task_desc}, {str(date_today)}, {str(TDD_formated)}, {task_complete}")
    tasks.close()

    print(f"\n{task_title} has been added to {task_person}\n")
def view_all():     #'va' View All Tasks 
        
    # The user would like to see all tasks.
    # This requires the following, simple for loop.

    task_file = open('tasks.txt', 'r')
    for line in task_file:
        if len(line.split(", ")) == 6:
            task_file = line.split(", ")
        
            print(f'''
_____________________________________________________
Task:           {task_file[1]}
Assigned to:    {task_file[0]}
Date assigned:  {task_file[3]}
Due date:       {task_file[4]}
Task complete:  {task_file[5]}
Task description:
{task_file[2]}
_____________________________________________________''')
def view_mine():    #'vm' View my Tasks
    while True:    
        # The user would like to see only their tasks.
        # This requires the following for loop and an
        # if statement to check if the task is the
        # users task and print it.

        task_file = open('tasks.txt', 'r')
        
        # A task number to assign to each task:
        task_number = 0
        # A list of all of all the numbered lists:
        numbered_tasks_list = []
        numbered_tasks_dict = {}
        # Go through every line in 'task_file'
        # to check if the current user 
        # is assigned to the task:
        for line in task_file:
            task_file = line.split(", ")
            
            if task_file[0] == current_username:
                
                # For each task the matches the user,
                # append to or increase the following variables:

                numbered_task = []
                task_number += 1
                numbered_task.append(task_number)

                numbered_task.append(line.strip())

                numbered_tasks_dict.update({task_number: line.strip()})
                numbered_tasks_list.append(list(numbered_task))

                # For each task given to the user,
                # print out all of the given data:
                print(f'''
Task {task_number}
_____________________________________________________
Task:           {task_file[1]}
Assigned to:    {task_file[0]}
Date assigned:  {task_file[3]}
Due date:       {task_file[4]}
Task complete:  {task_file[5]}
Task description:
{task_file[2]}
_____________________________________________________''')


    # Ask the user to enter a number that corresponds 
    # to a task or enter '-1' to return to the menu.
    
        try: 
            # User enters the number of the task they need:
            user_task_selection = int(input(\
            "Enter the task number you would like to edit (or enter -1 to return to menu): "))
        
            # A statement to check if the user selection is too big.
            if user_task_selection > len(numbered_tasks_dict):
                print("You don't have that many tasks.\n\nTry another number.")

            # A statement that gets the data from the dictioanry of tasks:
            elif user_task_selection > 0 and user_task_selection <= len(numbered_tasks_dict):
                
                choosen_task_unedited = numbered_tasks_dict.get(user_task_selection)
                choosen_task = choosen_task_unedited.split(", ")

                # Print out the information of given task:
                print(f'''
_____________________________________________________
Task:           {choosen_task[1]}
Assigned to:    {choosen_task[0]}
Date assigned:  {choosen_task[3]}
Due date:       {choosen_task[4]}
Task complete:  {choosen_task[5]}
Task description:
{choosen_task[2]}
_____________________________________________________
''')
                # Functions to ask the user if they would like 
                # the task marked as complete of incomplete:
                
                while True:
                    user_completion_selection = input(\
                        "Would you like to change the completion status of this task (Yes or No)? ")
                    if user_completion_selection.lower() == 'yes':

                        with open('tasks.txt', 'r') as x:
                            edit_task_file = x.readlines()
                   
                        tasks_list = []
                        # Strip and split each line from tasks.txt
                        # and append to tasks_list.
                        for line in edit_task_file:
                            edit_task_file = line.strip().split(", ")
                            tasks_list.append(edit_task_file)

                        new_task_list = []
                        # We will be editing an item within tasks.txt
                        # so we will need to rewrite all of the tasks.
                        # Because of this, we will create new_task_list
                        # which will keep track of all of the tasks
                        # within tasks.txt ready to re-write.
                        for task in tasks_list:
                            if task == choosen_task:

                                if task[5] == 'Yes':
                                    task[5] = 'No'
                                    new_task_list.append(task)
                                    print("Task completion changed.")

                                elif task[5] == 'Yes\n':
                                    task[5] = 'No'
                                    new_task_list.append(task)
                                    print("Task completion changed.")
                    
                                elif task[5] == 'No':
                                    task[5] = 'Yes'
                                    new_task_list.append(task)
                                    print("Task completion changed.")

                                elif task[5] == 'No\n':
                                    task[5] = 'Yes'
                                    new_task_list.append(task)
                                    print("Task completion changed.")

                            else:
                                new_task_list.append(task) 
                        
                        # Now we can re-write all of our tasks
                        # back into tasks.txt in the original
                        # format so we can access them again.
                        with open('tasks.txt', 'w') as x:
                            for line in new_task_list:
                                line = ', '.join(str(y) for y in line) + '\n'
                                x.write(line) 
                        break
                    elif user_completion_selection.lower() == 'no':
                        print("Okay.")
                        break

                    else:
                        print("Sorry, I didn't understand.\n\
                            Please enter 'Yes' or 'No.")
                continue
            
            # A statement to return the user to the menu:
            elif user_task_selection == -1:
                user_menu()

        
        # A value error incase the user doesn't enter an integer:
        except ValueError:
                print("Sorry, I don't understand what you entered.\nPlease enter a number.")
                continue
def gen_rep():      #'gr' Generate Reports

    # *** TASK OVERVIEW ***
    # The total number of tasks that have been generated and tracked using the task_manager.py:
    with open('tasks.txt', 'r') as lines:
        task_file_lines = len(lines.readlines())

    # Completed and uncompleted tasks
    task_file = open('tasks.txt', 'r')
    completed_tasks = 0
    uncompleted_tasks = 0
    num_task_file_lines = []
    for line in task_file:
            num_task_file_lines.append(line)
    num_task_file_lines = map(lambda s: s.strip('\n'), num_task_file_lines)
    for n in num_task_file_lines:
        if 'Yes' in n:
            completed_tasks += 1
        elif 'No' in n:
            uncompleted_tasks += 1
    task_file.close()

    # The total number of tasks that haven't been completed and that are overdue:
    task_status = []
    task_file = open('tasks.txt', 'r')
    for line in task_file:
        if len(line.split(", ")) == 6:
            task_file = line.split(", ")
            
            # Use enumerate to identify elements within each task...
            for idx, ele in enumerate(task_file):
                # ...and remove unwanted '\n'.
                task_file[idx] = ele.replace('\n', '')
            
            # Remove unwanted data:
            del task_file[0:4]
            
            # Append to 'task_status' so we can check the data.
            task_status.append(task_file)
            
            # Loop through 'task_status' 
            # so we can remove completed tasks:
            for n in task_status:
                if 'Yes' in n:
                    task_status.remove(n)
            del task_file[-1]
    
    # Convert list of lists to a smaller list
    task_status = [j for i in task_status for j in i]

    # Find overdue tasks by 
    # comparing due date 
    # to date today:
    overdue = 0
    updated_task_status = []
    for item in task_status:
        item = datetime.strptime(item, "%d %b %Y")
        updated_task_status.append(item)
        if item > datetime.now():
            overdue += 1

    # Find the percentage of tasks that are incomplete:
    task_file = open('tasks.txt', 'r')
    tasks_total = []
    for line in task_file:
        tasks_total.append(line)
    perc_incomp_tasks = (f"{getPercent(uncompleted_tasks, len(tasks_total), True)}%")
    task_file.close()

    # Find the percentage of tasks that are overdue:
    perc_overdue_tasks = (f"{getPercent(overdue, len(tasks_total), True)}%")


    # *** USER OVERVIEW ***
    
    # The total number of users registered with task_manager.py:
    with open('user.txt', 'r') as lines:
        user_file_lines = len(lines.readlines())

    # Write information to 'task_overview.txt'
    task_ov = open('task_overview.txt', 'w+')
    task_ov.write(f'''
_________________________________________________________________________________________
The total number of tasks that have been generated and tracked using the task_manager.py:
{task_file_lines}
The total number of completed tasks:
{completed_tasks}
The total number of uncompleted tasks:
{uncompleted_tasks}
The total number of tasks that have NOT been completed and that are overdue:
{overdue}
The percentage of tasks that are incomplete:
{perc_incomp_tasks}
The percentage of tasks that are overdue:
{perc_overdue_tasks}
_________________________________________________________________________________________
''')
    task_ov.close()

    # Write data to 'user_overiew.txt'
    user_ov = open('user_overview.txt', 'w+')
    user_ov.write(f'''
_________________________________________________________________________________________
The total number of users registered with task_manager.py:
{user_file_lines}
The total number of tasks that have been generated and tracked using task_manager.py:
{task_file_lines}
_________________________________________________________________________________________
''')
    user_ov.close()
    
    # *** INDIVIDUAL USER OVERIEWS ***
   
    # Create a list of tasks from 'tasks.txt'
    tasks_list = []
    task_file = open('tasks.txt', 'r')
    for line in task_file:
        tasks = line.split(', ')
        tasks_list.append(tasks)

    # Create a list of the users from 'users.txt'.
    users_list = []
    user_file = open('user.txt', 'r')
    for line in user_file:
        userAndpassword = line.split(', ')
        del userAndpassword[1]
        users_list.append(userAndpassword)

    # Convert list of lists to a simple list.
    users_list = [j for i in users_list for j in i]

    # Now it's time to collate the data ready to print per user.
    for user in users_list:

        # Create a count variable for all neccesary data to keep track:
        overdue = 0 
        plenty_of_time = 0
        user_complete_tasks = 0
        user_incomplete_tasks = 0
        user_total_tasks = 0

        # Begin task hunt 
        task_file = open('tasks.txt', 'r')
        for line in task_file:
            task_file = line.split(", ")
            
            # Use enumerate to identify elements within each task...
            for idx, ele in enumerate(task_file):
                # ...and remove unwanted '\n'.
                task_file[idx] = ele.replace('\n', '')
            
            # Run through tasks to check 
            # which task goes with which user.
            if task_file[0] == user:
                
                # Begin counting!
                # Total number of tasks:
                user_total_tasks += 1
                
                # If tasks is completed or not:
                if task_file[5] == 'Yes':
                    user_complete_tasks += 1
                elif task_file[5] == 'No':
                    user_incomplete_tasks += 1
                else:
                    continue
                
                # Compare due date of each item to date today
                # so we can know which tasks are overdue:
                task_file[4] = datetime.strptime(task_file[4], "%d %b %Y")
                if task_file[4] < datetime.now() and task_file[5] == 'No':
                    overdue += 1
                elif task_file[4] > datetime.now():
                    plenty_of_time += 1
                
        # Work out the percentages using 'getPercent' 
        # so we can format them into our user data table.
        if overdue == 0 and user_total_tasks == 0:
            percent_overdue = 0
        else:
            percent_overdue = getPercent(overdue, user_total_tasks, True)
        
        if user_total_tasks == 0 and user_complete_tasks == 0:
            percent_complete = 0 
        else:
            percent_complete = getPercent(user_complete_tasks, user_total_tasks, True)  

        if user_complete_tasks == 0 and user_incomplete_tasks == 0:  
            percent_incomplete = 0
        else:
            percent_incomplete = getPercent(user_incomplete_tasks, user_total_tasks, True)
        
        # Append our user data table per user to 'user_overview.txt':
        user_ov = open('user_overview.txt', 'a+')
        user_ov.write(f'''
_________________________________________________________________________________________
USER: {user}

The total number of tasks assigned to '{user}':
{user_total_tasks}
The percentage of the total number of tasks assigned to '{user}':
{getPercent(user_total_tasks, len(tasks_list), True)}%
The percentage of the tasks assigned to '{user}' completed:
{percent_complete}%
The percentage of the tasks assigned to '{user}' NOT completed:
{percent_incomplete}%
The percentage of the tasks assigned to '{user}' that are overdue:
{percent_overdue}%
_________________________________________________________________________________________
''')
        user_ov.close()

    # Ask the user whether they would like
    # to view the reports in terminal. 
    # This will then trigger the 'view_rep' function.
    user_vr = input("Would you like to view the reports?(Yes or No): ")
    while True:
        if user_vr.lower() == 'yes' or user_vr.lower() == 'y':
            view_rep()
            break
        elif user_vr.lower() == 'no' or user_vr.lower() == 'n':
            print("\nYou can view the reports at anytime with 'View Reports' at the menu.\n")
            break
        else:
            user_vr = input("Please enter either 'Yes' or 'No': ")
def view_rep():     #'vr' View Reports

    # Simple enough, this function will show both
    # the 'task_overview.txt' and 'user_overiew.txt' 
    # files in the terminal.
    with open('task_overview.txt', 'r') as user:
        print("\n*** CONTENTS OF TASK_OVERVIEW.TXT ***\n")
        print(user.read())
    with open('user_overview.txt', 'r') as user:
        print("\n*** CONTENTS OF USER_OVERVIEW.TXT ***\n")
        print(user.read())
def display():      #'ds' Tasks and User Statistics 
        if current_username == 'admin':

            # The admin would like to see the number of tasks and users.
            # These lines of code will show only to the admin and will
            # print out the number of lines in tasks.txt and user.txt.
            print('_____________________________________________________')
            with open('user.txt', 'r') as user:
                admin_stats = len(user.readlines())
                if admin_stats > 1:
                    print(f"\nThere are {admin_stats} users saved to file.\n")
                elif admin_stats == 1:
                    print(f"\nThere is {admin_stats} user saved to file.\n")
                else:
                    print("There are no users saved to file.\n")
            with open('tasks.txt', 'r') as user:
                tasks_stats = len(user.readlines())
                if tasks_stats > 1:
                    print(f"There are {tasks_stats} tasks saved to file.\n")
                elif tasks_stats == 1:
                    print(f"There is {tasks_stats} task saved to file.\n")
                else:
                    print("There are no tasks saved to file.\n")
            print('_____________________________________________________')
def exit_menu():    #'e' Exit

        print(f'Goodbye {current_username.capitalize()}!!!')
        exit()


# ===== LOGIN SECTION =====

# Open the user file to collect username & password
in_file = open('user.txt', 'r')
user = in_file.readlines()
in_file.close()


# Open the task file to collect tasks
in_file = open('tasks.txt', 'r')
tasks = in_file.readlines()
in_file.close()


# Trigger User Menu function:
user_menu()