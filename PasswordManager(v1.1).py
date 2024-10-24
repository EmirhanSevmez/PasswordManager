from time import sleep
import random
import string
from cryptography.fernet import Fernet   # Importing Fernet from cryptography.fernet
import os
def move_to_appdata():
    appdata_path = os.getenv('APPDATA') # Getting the appdata path
    os.chdir(appdata_path) # Changing the directory to the appdata path




def generate_key(): #   Function to generate a key
    key = Fernet.generate_key() # Generating a key
    with open("sec.key", "wb") as file: # Opening the file in write binary mode
        file.write(key) # Writing the key to the file
    
def encrypt(): # Function to encrypt the password
    with open("sec.key", "rb") as file: # Opening the file in read binary mode
        key = file.read() # Reading the key from the file
    cipher_suite = Fernet(key) # Creating a cipher suite object
    with open("windows.txt", "rb") as file: # Opening the file in read binary mode
        data = file.read() # Reading the data from the file
    encrypted_data = cipher_suite.encrypt(data) # Encrypting the data
    with open("windows.txt", "wb") as file: # Opening the file in write binary mode
        file.write(encrypted_data) # Writing the encrypted data to the file
        
    
def decrypt(): # Function to decrypt the password
    with open("sec.key","rb") as file: # Opening the file in read binary mode
        key = file.read() # Reading the key from the file
    cipher_suite = Fernet(key) # Creating a cipher suite object
    with open("windows.txt", "rb") as file: # Opening the file in read binary mode
        encrypted_data = file.read() # Reading the encrypted data from the file
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode() # Decrypting the data
    with open("windows.txt", "w") as file: # Opening the file in write mode
        file.write(str(decrypted_data)) # Writing the decrypted data to the file



def Add(): # Function to add a new password
    username = input("Enter Username: ")   # Reading the username from the user
    password = input("Enter Password: ") # Reading the password from the user
    if not username.strip() or not password.strip(): # Checking if the username or password is empty
        print("Username or Password cannot be empty") # Printing an error message
        return # Returning from the function
    else: # If the username and password are not empty
        with open("windows.txt", "a") as f: # Opening the file in append mode
            f.write(f"{username} {password}\n") # Writing the username and password to the file
            print("Password Added Successfully") # Printing a success message
def delete(): # Function to delete a password
    username = input("Enter Username: ") # Reading the username from the user
    if not username.strip(): # Checking if the username is empty
            print("Username cannot be empty") # Printing an error message
            return # Returning from the function
    with open("windows.txt", "r") as f: # Opening the file in read mode
        lines = f.readlines() # Reading all the lines from the file
    with open("windows.txt", "w") as f: # Opening the file in write mode
        for line in lines: # Iterating over each line
            if username not in line: # Checking if the username is not in the line
                f.write(line) # Writing the line to the file
        print("Password Deleted Successfully") # Printing a success message
def list(): # Function to list all the passwords
    with open("windows.txt", "r") as f: # Opening the file in read mode
        print(f.read()) # Reading and printing all the lines from the file
def show(): # Function to show a password
    username = input("Enter Username: ") # Reading the username from the user
    with open("windows.txt", "r") as f: # Opening the file in read mode
        lines = f.readlines() # Reading all the lines from the file
    for line in lines: # Iterating over each line
        if not username.strip(): # Checking if the username is empty
            print("Password Not Found") # Printing an error message
        elif username in line: # Checking if the username is in the line
            print(line) # Printing the line
        else: # If the username is not in the line
            print("Password Not Found") # Printing an error message
def RandomAdd(): # Function to add a random password
    characters = string.ascii_letters + string.digits + string.punctuation # Defining the characters to be used in the password
    password = ''.join(random.choice(characters) for i in range(10)) # Generating a random password of length 10
    username = input("Enter Username: ") # Reading the username from the user
    with open("windows.txt", "a") as f: # Opening the file in append mode
        f.write(f"{username} {password}\n") # Writing the username and password to the file
        print("Password Added Successfully") # Printing a success message
 

def CleanSpace():
    with open("windows.txt", "r") as f: # Opening the file in read mode
        lines = f.readlines() # Reading all the lines from the file
        cleanlines = [line.strip() for line in lines if line.strip()] # Removing any empty lines
    with open("windows.txt", "w") as f: # Opening the file in write mode
        f.writelines(cleanlines) # Writing the clean lines to the file
        
move_to_appdata() # Moving the file to the appdata folder
        
try:
    with open("sec.key", "rb") as key_file: # Opening the key file in read binary mode
        key = key_file.read() # Reading the key from the file
except FileNotFoundError: # If the key file is not found
    generate_key()
try:
    with open("windows.txt", "rb") as password_file:# Opening the password file in read binary mode
        password_file.read() # Reading the password file
    decrypt()
        
except FileNotFoundError: # If the password file is not found
    with open("windows.txt", "w") as password_file: # Opening the password file in write mode
        password_file.write("") # Writing an empty string to the file
        


    
    
    
    
while True: # While loop to keep the program running
    print("Loading...") # Printing a loading message
    sleep(1) # Sleep for 1 second
    
    try: # 
        print("Welcome to Password Manager App. Please select one option")
        print("1) Add New 2) Delete Password 3) List All Passwords 4) Show Specific Password 5) Exit")
        i = int(input("Input a number: "))
        
        if i==1: # If the user selects option 1
            x=int(input("1) Random Password 2) Custom Password: "))
            if x==1: # If the user selects option 1
                RandomAdd() # Call the RandomAdd function
            elif x==2: # If the user selects option 2
                Add() # Call the Add function
        elif i==2: # If the user selects option 2
            delete() # Call the delete function
        elif i==3: # If the user selects option 3
            list() # Call the list function
        elif i==4: # If the user selects option 4
            show() # Call the show function
        elif i==5: # If the user selects option 5
            print("Exiting...") # Print a message
            break # Break the loop
    except KeyboardInterrupt: # If the user presses Ctrl+C
        print("Exiting...") # Print a message
        break # Break the loop
    except: # If an error occurs
        print("Invalid Input") # Print a message
CleanSpace() # Call the CleanSpace function
encrypt() # Encrypting the file
      


