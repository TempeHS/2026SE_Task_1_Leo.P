#register the user

def menu():
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    selection = input("Select an option: ")
    if selection == 1:
        login()
    elif selection == 2:
        register()
    elif selection == 3:
        quit()
    else:
        print("You have chosen an unsupported number.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

def register():
    chosen_username = input("Choose a username: ")
    chosen_password = input("Choose a password: ")

def quit():
    exit()

menu()


# ask user for their username and password

##username = input("Enter username: ")
##password = input("Enter password: ")




# minimum 4 character password


    