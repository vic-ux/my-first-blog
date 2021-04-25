# register
# - username, email and password
# - generate user id
# - 


# login
# - (username or email) and password

#bank operation


import random
from random import randint
import time
import datetime


database = {}

def init():
    print ("Welcome to bankPHP")
    
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no)\n"))
    
    if (haveAccount == 1):
        login()
        
    elif (haveAccount == 2):
        register()
        
    else:
        print("You have selected an invalid option.")
        init()
    
def login():
    accountLogin = int(input("Enter your account number: \n"))
    password = input("Enter your password: \n")
    for accountNumber, userDetails in database.items():
        if accountNumber == accountLogin and userDetails[3] == password:
            bankOperation(userDetails)
        
        else:
            print("Account number and password does not match.")
            moment = datetime.datetime.now()
            print(moment.strftime("%d-%b-%Y %I:%M:%S %p\n"))
            login()
                
    print("invalid account or password")
    moment = datetime.datetime.now()
    print(moment.strftime("%d-%b-%Y %I:%M:%S %p\n"))
    login()
    
def register():
    print ("Welcome to the registration page")
    email = input("Enter an email address: \n")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    password = input ("Enter a unique password: \n")
    password2 = input("Re-enter your password: \n")
    
    if (password == password2):
        accountNumber = generationAccountnumber()
        database[accountNumber] = [first_name, last_name, email, password]
        
        print("Your registration was successful...")  
        print(f"Your account number is : {accountNumber}")
        moment = datetime.datetime.now()
        print(moment.strftime("%d-%b-%Y %I:%M:%S %p\n"))
        print ("You can proceed to login.")  
        
        login()
    else:
        print ("password does not match.")
        register()
        
def bankOperation(userDetails):
    
    print(f"Welcome, {userDetails[0], userDetails[1]}")
    moment = datetime.datetime.now()
    print(moment.strftime("%d-%b-%Y %I:%M:%S %p\n"))
    print ("These are the available options:\n")
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('0. Exit\n')
    selectedOption = int(input ('Please select an option: \n'))
        
    if (selectedOption == 1):
        withdrawalOperations()
        
    elif (selectedOption == 2):
        depositOperations()
        
    elif (selectedOption == 3):
        complaintPlatform()
        
    elif (selectedOption == 4):
        print("You have successfully logged out")
        login()
        
    elif (selectedOption == 0 ):
        print("process finished with exit code 0")
        exit()
        
    else:
        print ('Invalid Option selected, please try again.')
        bankOperation(userDetails)

    
def withdrawalOperations():
    withdraw = int(input ('How much would you like to withdraw? \n'))
    print(f'The sum of NGN{withdraw} was debited from your account.\n')
    
    transact = int(input("Do you wish to perform another transaction?  1 (yes)  2 (no)\n"))
    if (transact == 1):
        login()
        
    elif (transact == 2):
        exit()
        
    else:
        print('invalid operation')
        exit()
        
def depositOperations():
    deposit = int(input ('How much would you like to deposit? \n'))
    print(f' You deposited the sum of NGN{deposit} only.\n')
    transact = int(input("Do you wish to perform another transaction?  1 (yes)  2 (no)\n"))
    
    if (transact == 1):
        login()
        
    elif (transact == 2):
        exit()
        
    else:
        print('invalid operation')
        exit()
    
def complaintPlatform():
    complaint = input('What issue will you like to report? \n')
    print('Thank you for contacting us.\n')
    
    transact = int(input("Do you wish to perform another transaction?  1 (yes)  2 (no)\n"))
    
    if (transact == 1):
        login()
        
    elif (transact == 2):
        exit()
        
    else:
        print('invalid operation')
        exit()


def generationAccountnumber():
    acct_numGen = randint (1111111111,9999999999)
    wait_time = random.randint(1,5)
    time.sleep(wait_time)
    return (acct_numGen)
    

init ()