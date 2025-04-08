# user logs in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

# register user
def register():
    chosen_username = input("Choose a username: ")
    chosen_password = input("Choose a password: ")
    if chosen_password < 4:
        i = chosen_password
        while i < 4:
            print("Your password must be a minimum of 4 characters.")
    else:
        with open("plain_text.txt", "a") as file:
	        file.write(f"{chosen_username}, {Chosen_password}\n")

# quit option
def quit():
    exit()

# User is offered a menu
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

menu()