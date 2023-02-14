"""
Customer Registration and Information
Writer: Murat Can Olgunsoy
Revision Date: 14.02.2023
"""
import pandas as pd

data = pd.read_csv("customers.csv",encoding= 'unicode_escape')

def getData(customerId):
    data = pd.read_csv("customers.csv",encoding= 'unicode_escape')
    global row
    flag=0
    row=0

    while row<=(len(data.index)-1):
        if(customerId == str(data.loc[row, "ID"])):
            rem = row
            flag = 1
        row = row + 1
    if(flag == 1):
        row = rem
        return 1
    else:
        return 0    

def checkId():
    customerId = input("Identification Number: ")
    flag = getData(customerId)
    if (flag == 1):
        signIn(customerId)
    elif (flag == 0):
        flag = int(input("There is no existed customer for that ID Number. Enter 0 to sign up, 1 to try sign in again."))
        if (flag==0):
            signUp(customerId)
        elif (flag==1):
            checkId()

def signIn(ID):
    password = str(input("Password: "))
    if (password == str(data.loc[row,"Password"])):
        print("Hoşgeldin "+"".join(str(data.loc[row,"Name"]))+" "+"".join(str(data.loc[row,"Last Name"])))
        customerService()
    else:
        flag = int(input("Wrong password. 1 to try again or 2 to exit: "))
        if(flag == 1):
            checkId()
        elif(flag == 2):
            exit

def signUp(customerId):
    customerName = input("Enter your name: ")
    customerLastname = input("Enter your lastname: ")
    customerMail = input("Enter your mail adress: ")
    customerBirthday = input("Enter your birthday as DD/MM/YYYY : ")
    customerPassword = input("Enter your password: ")

    customer = {
        'Name':[str(customerName)],
        'Lastname':[str(customerLastname)],
        'ID':[str(customerId)],
        'Mail':[str(customerMail)],
        'Birthday':[str(customerBirthday)],
        'Balance':0,
        'Password':[str(customerPassword)],
        'Password2':["NaN"],
        'Password3':["NaN"]}
    df = pd.DataFrame(customer)
    df.to_csv("customers.csv",mode='a', index=False, header=False)
    print("Data appended successfully.")
    flag = int(input("1 to sign in or 0 to exit."))
    if(flag == 1):
        checkId()
    elif(flag == 0):
        exit
def customerService():
    selection = int(input("\n\t1 ---> Withdraw Money\n\t2 ---> Deposit Money\n\t3 ---> Change Password\n\t4 ---> Exit\nEnter your selection : "))
    if(selection == 1):
        withdraw()
        
    elif(selection == 2):
        deposit()
        
    elif(selection == 3):
        changePassword()

    elif(selection == 4):
        exit

def withdraw():
    print("Balance= "+"".join(str(data.loc[row,"Balance"])))
    amount = int(input("How much do you want to withdraw: "))
    if(amount<=int(data.loc[row,"Balance"])):
        balance = int(data.loc[row,"Balance"])-amount
        data.loc[row,"Balance"] = balance
        data.to_csv("customers.csv", index=False)
        print("Withdraw is done.")
        customerService()
    else:
        flag = int(input("Insufficient balance! 1 to try withdraw again, 2 to back main menu: "))
        if(flag == 1):
            withdraw()
        elif(flag == 2):
            customerService()

def deposit():
    print("Balance= "+"".join(str(data.loc[row,"Balance"])))
    amount = int(input("How much do you want to deposit: "))
    balance = int(data.loc[row,"Balance"])+amount
    data.loc[row,"Balance"] = balance
    data.to_csv("customers.csv", index=False)
    print("Deposit is done.")
    customerService()

def changePassword():
    newPassword = input("New password : ")
    
    if(str(data.loc[row,"Password2"]) == newPassword ):        
        selection = int(input("The new password has to be different form your last two passwords.\n1 to try again, 0 to exit."))
        if(selection == 1):
            changePassword()
        elif(selection == 0):
            exit  
    elif (str(data.loc[row,"Password3"]) == newPassword ):
        selection = int(input("The new password has to be different form your last two passwords.\n1 to try again, 0 to exit."))
        if(selection == 1):
            changePassword()
        elif(selection == 0):
            exit
    elif (str(data.loc[row,"Password"]) == newPassword ):
        selection = int(input("The new password has to be different form your current password.\n1 to try again, 0 to exit."))
        if(selection == 1):
            changePassword()
        elif(selection == 0):
            exit
    else:
        data.loc[row,"Password3"] = str(data.loc[row,"Password2"])
        data.loc[row,"Password2"] = str(data.loc[row,"Password"])
        data.loc[row,"Password"] = str(newPassword)
        data.to_csv("customers.csv", index = False)
        
        
        selection = int(input("Password has changed.\n1 to back to menu, 0 to exit.\n"))
        if(selection == 1):            
            customerService()
        elif(selection == 0):
            exit

#--------------------------------------------------------------------------
print("---------------Bank Of MCO---------------")
checkId()


