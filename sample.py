#creating and opening a file in append mode
file_name = "c:/Workspace/Angel/DataAnalyst/Microsoft VS Code/1-Python basics/credentials.txt"
   
   # Check if text file exists, if not, create one
open(file_name, 'a').close()



           
def add_credentials(file_name):
   """Add and store credentials to the file."""
   username = input("Enter the username: ")
   password = input("Enter the password: ")
   url = input("Enter the URL/resource: ")
         
   with open(file_name, "a") as file:  # Append mode
       file.write(f"{username},{password},{url}\n")

#view the stored the stored credentials
def view_credentials(file_name):
   """Display the stored credentials in a visually presentable way."""
   with open(file_name, "r") as file:
              
       for line in file:
           uname,pword,url1= line.split(',')
           print(f"{uname}\t{pword}\t{url1}")


def menu():
    """Display the options menu."""
while True:   
    print("\n Options Menu:")
    print("1. Add credentials.")
    print("2. View credentials.")
    print("3. Exit the script.")
    choice = input("Enter your choice: ")
    if choice == "1":
     add_credentials(file_name)
    elif choice == "2":
      view_credentials(file_name)
    elif choice == "3":
     print("Exit!")
     break
menu()