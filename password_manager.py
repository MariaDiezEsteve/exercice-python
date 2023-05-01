#The point of this program is to king of organize and store our passwords. So we're going to store all of the passwords aoong with the username of the account they're associated with any text file. And we're going to encrypt the passwords. 
#We're going to use master password for all the pw but it is not recommend to do it. 

#To use the module to encrypt the password:
#https://cryptography.io/en/latest/fernet/
'''from cryptography.fernet import Fernet

 def write_key():
    
    key = Fernet.generato_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key) '''

#Ask the user to a master pw whether they want to list out their passwords or if they want to add a new one. 

master_pwd =  input("What is the master password?") #We're going to use pwd to encrypt our pw

#If pwd is not correct, the program is not going to show the correct pw
#We ask what mode it's going to choose, if the want to add a new password or if they want to view their passwords

#We need to define what means(what kind of funtionality has)

def add():
    #We want to create a new file if the file storing our password is doesn't already exist and add the pw into it.
    name = input("Account name: ")
    pwd = input("Password: ")
    
    #The open() function opens a file, and returns it as a file object. open(file, mode) --The path and name of the fileand the mode:
        #https://www.w3schools.com/python/ref_func_open.asp
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
    # "a" - Append - Opens a file for appending, creates the file if it does not exist. 
    #"w" - Write - Opens a file for writing, creates the file if it does not exist
    #"x" - Create - Creates the specified file, returns an error if the file exist
    #"t" - Text - Default value. Text mode
    #"b" - Binary - Binary mode (e.g. images)
    
    with open("passwords.txt", "a") as f: #with: Automatically open and close the file
        f.write(name + "|" + pwd + "\n") #\n add a line break
        '''  f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")'''
        
def view():
      with open("passwords.txt", "r") as f: 
            for line in f.readlines():
              #print(line) - This print, print one more line so we want to solve that. 
              #print(line.rstrip()) 
              #The rstrip() method removes any trailing characters (characters AT THE END a string), space is the default trailing character to remove. string.rstrip(characters)
                data = line.rstrip() #to separate the name to the pw
                user, passw = data.split("|")
              #The split() method splits a string into a list. string.split(separator, maxsplit)
              #txt = "welcome to the jungle" x = txt.split()
              #print(x) --- ['welcome', 'to', 'the', 'jungle']
                print("User: ", user, ", Password: ", passw)
                '''   print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())'''
            
while True:
    mode = input("Would you like to add a new password or wiew existing ones (view, add)?").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue

#to encrypt the password:
#Terminal: pip install cryptography