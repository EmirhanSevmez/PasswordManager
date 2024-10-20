import tkinter as tk
from tkinter import messagebox
def Add():
    ## input username
    username = entryName.get()
    ## input password
    password = entryPassword.get()
    if username and password:
        with open ("passwords.txt", "a") as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success"," Password added")
    else:
        messagebox.showerror("Error", "Please enter both the fields")
        
def get():
    # input from user
    username = entryName.get()
    
    # creating a dictionary to store the data in the form of key-value pairs
    passwords = {}
    
    try:
        # open text file
        with open("passwords.txt","r") as f:
            for k in f:
                i = k.split(" ")
                passwords[i[0]] = i[1]
                
    except:
        print("ERROR!")
        
    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No such username exists !!"
        messagebox.showinfo("Passwords",mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST")
        
        
def delete ():
    # accepting input from the user
    username = entryName.get()
    # creating temp list
    temp_passwords = []
        
    try:
        with open("passwords.txt","r") as f:
              for k in f:
                  i = k.split(" ")
                  if i[0] != username:
                     temp_passwords.append(f"{i[0]} {i[1]}")
                      
        with open("passwords.txt","w") as file:
            for line in temp_passwords:
                file.write(line)

        messagebox.showinfo("Success",f"User {username} deleted succesfully")
    except Exception as e:
        messagebox.showerror("Error",f"Error deleting user {username}: {e}")
            
def getList():
    # creating a dictionary to store the data in the form of key-value pairs
    passwords = {}
    
    try:
        # open text file
        with open("passwords.txt","r") as f:
            for k in f:
                i = k.split(" ")
                passwords[i[0]] = i[1]
                
    except:
        print("ERROR!")
    if passwords:   
        mess = "Your passwords:\n"
        for name,password in passwords.items(): 
            mess += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords",mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST")
        


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("250x170")
    app.title("Password Manager")
    
    #Username block
    labelName = tk.Label(app, text= "USERNAME: ")
    labelName.grid(row=0,column=0,padx=15,pady=15)
    entryName = tk.Entry(app)
    entryName.grid(row=0, column=1,padx=10,pady=15)
    
    ##Password block
    labelPassword = tk.Label(app, text= "PASSWORD: ")
    labelPassword.grid(row=1, column=0, padx=10,pady=5)
    entryPassword = tk.Entry(app)
    entryPassword.grid(row=1,column=1,padx=10,pady=5)
    
    # Add button
    buttonAdd = tk.Button(app, text="Add", command=Add)
    buttonAdd.grid(row=2, column=0,padx=15,pady=8,sticky="we")
    
     # Get button
    buttonGet = tk.Button(app, text="Get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=0, padx=15, pady=8, sticky="we")
    
    ## List button
    buttonList = tk.Button(app, text="List",command=getList)
    buttonList.grid(row=3, column=1,padx=15,pady=8,sticky="we")

    app.mainloop()                
    