'''
task 3
using the txt file to save the input.'''


# def read():
#  a=int(input('would you like to sign in or sign up(1=in/2=up):'))
#  if a==1 :
#      username=input("enter username:")
#      password=input("enter password:")
#      mobileNumber=input("enter mobile number:")
#      with open('database1.txt','w') as f:
#         f.write(username+' '+password+' '+mobileNumber)
#  elif a==2 :
#         username=input("enter username:")
#         password=input("enter password:")
#         mobileNumber=input("enter mobile number:") 
#         with open('database1.txt','r') as f:
#             readNOte=f.readlines()
        
#         found =False
#         for note in readNOte:
#          if note.strip() == (username+' '+password+' '+mobileNumber):
#                print("welcome inside the server")
#                found =True
#                break
#         else:
#             print("the detail is incorrect")
    
#  else:
#     print("invalid input")

# while True: 
#     b = input("Would you like to enter the server (yes/no): ").lower()
#     if b == "yes":
#         read()
#     elif b == "no":
#         print("Thank you for visiting")
#         break
#     else:
#         print("Invalid input. Please enter 'yes' or 'no'.")


'''
saving the file in the jason file'''
import json
import os

def read():
    a = int(input('Would you like to sign in or sign up (1=in/2=up): '))
    
    if a == 1:  # Sign up
        username = input("Enter username: ")
        password = input("Enter password: ")
        mobileNumber = input("Enter mobile number: ")
        
        if os.path.exists('database1.json'):
            with open('database1.json', 'r') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []
        
        users.append({
            "username": username,
            "password": password,
            "mobileNumber": mobileNumber
        })
        
        with open('database1.json', 'w') as f:
            json.dump(users, f)
        
        print("You have successfully signed up!")
    
    elif a == 2:  # Sign in
        username = input("Enter username: ")
        password = input("Enter password: ")
        mobileNumber = input("Enter mobile number: ")
        
        if os.path.exists('database1.json'):
            with open('database1.json', 'r') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []
        
        found = False
        for user in users:
            if user["username"] == username and user["password"] == password and user["mobileNumber"] == mobileNumber:
                print("Welcome inside the server!")
                found = True
                break
        
        if not found:
            print("The details are incorrect.")
    
    else:
        print("Invalid input")

while True: 
    b = input("Would you like to enter the server (yes/no): ").lower()
    if b == "yes":
        read()
    elif b == "no":
        print("Thank you for visiting")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
