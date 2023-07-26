# Create a login page backend to ask users to enter the username and password.
# ask for a Re-Type Password and if the password is incorrect give a chance to enter it again but it should not be more than 3 times

def login_backend():
    max_attempts = 3
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    attempts = 0

    while attempts < max_attempts:

        retype_password = input("Re-type your password: ")

        if  password == retype_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    print("Maximum attempts reached. Login failed.")
    return False

login_backend()
