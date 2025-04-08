# load menu with login, register, quit

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("plain_text.txt", "w")
	file.write(username)
	file.close()

login()

# ask user for their username and password

##username = input("Enter username: ")
##password = input("Enter password: ")

# register user 

##chosen_username = input("Choose a username: ")
##chosen_password = input("Choose a password: ")

# minimum 4 character password

##if chosen_password > 4:
    ##print("Password must be a minimum of 4 characters.")

##else:
    ##print("")