import codecs
def display_menu():
   """Display the options menu."""
   print("\nOptions Menu:")
   print("1. Add credentials.")
   print("2. View credentials.")
   print("3. Exit the script.")
   choice = input("Enter your choice: ")
   return choice

def add_credentials(file_name):
   """Add and store credentials to the file."""
   username = input("Enter the username: ")
   password = input("Enter the password: ")
   url = input("Enter the URL/resource: ")
   encryptedUserName=codecs.encode(username,'rot13')
   print(type(encryptedUserName))
   encryptedPassword=codecs.encode(password,'rot13')
   encryptedUrl=codecs.encode(url,'rot13')
  
   
   with open(file_name, "a") as file:  # Append mode
       file.write(f"{encryptedUserName},{encryptedPassword},{encryptedUrl}\n")

def view_credentials(file_name):
    with open(file_name, "r") as file:
       print("\nStored Credentials:")
       print("-" * 40)
       print("Username\tPassword\tURL/Resource")
       print("-" * 40)
       
       for line in file:
           uname,pword,url1= line.strip().split(',')
         #  print(uname)
         #  decryptedUserName=rot13(uname)
          # decryptedUserName=codecs.decode(uname,'rot13')
          # print(decryptedUserName)
          # decryptedPassword=codecs.decode(pword,'rot13')
          # decryptedUrl=codecs.decode(url1,'rot13')2

          
           print(f"{uname}\t{pword}\t{url1}")
def main():
   file_name = "c:/Workspace/Angel/DataAnalyst/Microsoft VS Code/1-Python basics/credentials.txt"
   
   # Check if text file exists, if not, create one
   open(file_name, 'a').close()
   
   while True:
       choice = display_menu()
       
       if choice == "1":
           add_credentials(file_name)
       elif choice == "2":
           view_credentials(file_name)
       elif choice == "3":
           print("Exiting script. Goodbye!")
           break
       else:
           print("Invalid choice. Please select again.")

if __name__ == "__main__":
   main()