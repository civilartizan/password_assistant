import sys
import pyperclip
import json
import time  # # Module required for timing.

# Specify the name and location of the password.txt file that will be used as database.
PASSWORDS_FILE = r"C:\Users\ismai\PycharmProjects\password_assistant\passwords.txt"

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}  # If the file is not found, create an empty dictionary.
    return passwords

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

def main():
    while True:  # Create a loop.
        PASSWORDS = load_passwords()

        user_input = str(input(' Enter the username to retrieve the password.\n   Or,\n Enter "<username> <password>" to save a new entry.\n   Or,\n Enter "list" to display all saved passwords.\n\n   :'))
        inputs = user_input.split()
        number_of_input = len(inputs)

        if number_of_input == 2:
            account, password = inputs[0], inputs[1]
            PASSWORDS[account] = password
            save_passwords(PASSWORDS)
            print(account + "\n\n                                       {account} Has been saved successfully.\n")
        elif number_of_input == 1:
            account = user_input
            if account == "list":
                print(PASSWORDS)
                print("\n" * 1)
            elif account in PASSWORDS:
                pyperclip.copy(PASSWORDS[account])
                print(account + "                                        Password for {account} copied to clipboard.")
                # Close the program after 3 seconds.
                time.sleep(3)
                sys.exit()
            else:
                print('                                       No entry found for the given username.\n')
                continue
        else:
            print('\n\n                                       !!!  Invalid input  !!!\n')
            continue

if __name__ == "__main__":
    main()
