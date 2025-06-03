def greeting(name):
  print("Hello, " + name)
           
def add_credentials(file_name):
  try: 
   """Add and store credentials to the file."""
   username = input("Enter the username: ")
   password = input("Enter the password: ")
   url = input("Enter the URL/resource: ")
       
   with open(file_name, "a") as file:  # Append mode
       file.write(f"{username},{password},{url}\n")
  except FileNotFoundError:
      print("File not created")
     
   
  
#view the stored the stored credentials
def view_credentials(file_name):
  try:
   """Display the stored credentials in a visually presentable way."""
   with open(file_name, "r") as file:
              
       for line in file:
           uname,pword,url1= line.split(',')
           print(f"{uname}\t{pword}\t{url1}")
  except FileNotFoundError:
     print("File not created for reading")