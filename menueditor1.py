'''
Feedback:

Hi Angel, Your pseudocode looks great and covers all the necessary steps for writing the script for the Password Manager for DigiCore.

I have also executed your Python script. Could you please modify it to display a confirmation message stating 'Credentials have been added to the file' once the user has provided their username, password, and URL?
'''


import os
import filefunctions
#creating and opening a file in append mode
file_name = "c:/Workspace/Angel/DataAnalyst/Microsoft VS Code/1-Python basics/funpack/credentials.txt"
   
   # Check if text file exists, if not, create one
open(file_name, 'a').close()

def menu():
    """Display the options menu."""
while True:   
    print("\n Options Menu:")
    print("1. Add credentials.")
    print("2. View credentials.")
    print("3. Exit the script.")
    choice = input("Enter your choice: ")
    if choice == "1":
     filefunctions.add_credentials(file_name)
    elif choice == "2":
       if os.path.getsize(file_name) == 0:
         print(f"The file '{file_name}' is empty.")
       else:
        filefunctions.view_credentials(file_name)
    elif choice == "3":
     print("Exit!")
     break
    else:
      print("Please enter the correct choice")
    
menu()
