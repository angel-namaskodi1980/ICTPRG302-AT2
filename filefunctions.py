def is_dot(char):
    """Checks if a character is a dot.

    Args:
        char: The character to check.

    Returns:
        True if the character is a dot, False otherwise.
    """
    return char == '.'         
def add_credentials(file_name):
  try: 
   """Add and store credentials to the file."""
   username =input("Enter the username: ").upper()
   password = input("Enter the password: ").upper()
   url = input("Enter the URL/resource: ").upper()
       
   with open(file_name, "a") as file:  # Append mode
       encrypteduname=rot3_encrypt(username)
       encryptedpword=rot3_encrypt(password)
       encryptedurl=rot3_encrypt(url)
       file.write(f"{encrypteduname},{encryptedpword},{encryptedurl}\n")
  except FileNotFoundError:
      print("File not created")
     
   
  
#view the stored the stored credentials
def view_credentials(file_name):
  try:
   """Display the stored credentials in a visually presentable way."""
   with open(file_name, "r") as file:
              
       for line in file:
           uname,pword,url1= line.split(',')
           decrypteduname=rot3_decrypt(uname)
           decryptedpword=rot3_decrypt(pword)
           decryptedurl=rot3_decrypt(url1)
           print(f"{decrypteduname}\t{decryptedpword}\t{decryptedurl}")
  except FileNotFoundError:
     print("File not created for reading")
  # Dictionary to lookup the index of alphabets
dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26 }
    # Dictionary to lookup alphabets 
# corresponding to the index after shift
dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}
  
def rot3_encrypt(text):
    """
    Apply a simple ROT3 encryption to the text.
    Shifts letters and digits by 3 positions.
    """
  
    cipher = ''
    for letter in text:
        # print(type(letter))
        # checking for space
        flag=is_dot(letter)
        if(flag == True): # replace '.' with ' . '
         cipher+= '.'

        elif(letter != ' ' ):
            # looks up the dictionary and 
            # adds the shift to the index
            num = ( dict1[letter] + 3 ) % 26
            # looks up the second dictionary for 
            # the shifted alphabets and adds them
            cipher += dict2[num]
        
        else:
            # adds space
            cipher += ' '

    return cipher

def rot3_decrypt(text):
    """
    Decrypts ROT3-encrypted text by reversing the shift.
    """
    decipher = ''
    text1=text.strip()
    for letter in text1:
        # checks for space
        flag=is_dot(letter)
        if(flag == True): # replace '.' with ' . '
         decipher+= '.'
        
        elif(letter != ' '):
            # looks up the dictionary and 
            # subtracts the shift to the index
            num = ( dict1[letter] - 3 + 26) % 26
            # looks up the second dictionary for the 
            # shifted alphabets and adds them
            decipher += dict2[num]
        else:
            # adds space
            decipher += ' '

    return decipher




















