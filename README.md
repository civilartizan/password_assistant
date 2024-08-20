# Password Assistant

Tired of searching your passwords in your secret vault every time you need them?
A simple Python-based password manager that allows users to store, retrieve, and copy passwords securely. 
Easily manage and access your credentials with this lightweight tool.

## Libraries Used
- **sys**: For accessing command-line arguments.
- **pyperclip**: For copying passwords to the clipboard.
- **json**: For saving and loading password data from a text file.

## Key Features
- Add new username-password pairs.
- Retrieve passwords for existing usernames.
- Copy the password to the clipboard for easy access.
- List all saved passwords in the archive.

## Lessons Learned
- **Working With IDE**: PyCharm IDE is used in creating and uploading the project.
- **File Handling**: Gained experience in reading from and writing to files using Python.
- **JSON**: Learned how to store data in JSON format and how to handle file errors.
- **Virtual Environments**: Used `venv` to manage project dependencies.
- **Git & GitHub**: Practiced version control and uploading projects to GitHub for sharing and collaboration.

## Installation
Open your terminal and follow the steps below.
1. Clone the repository.
  git clone https://github.com/civilartizan/password_assistant.git
2. Create a virtual environment and activate it.
  python -m venv venv
  source venv/bin/activate  # For Mac/Linux
  venv\Scripts\activate  # For Windows
3. Install the required dependencies:
  pip install -r requirements.txt
4. Change the "PASSWORD" file location manually in main.py
