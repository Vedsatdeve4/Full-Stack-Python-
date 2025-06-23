balance = 0

def check_bal():
    print("Total balance = ", balance)

def deposit(amt):
    global balance
    balance += amt
    print(amt,"rs deposited")

def withdraw(amt):
    global balance
    if balance >= amt:
        balance -= amt
        print(amt,"rs withdraw")
        
    else:
        print("Not sufficient money, your current balance:", balance)
       
   


while True:
    ch = int(input("\n Enter your choice: \n1.Deposit Cash \n2.Withdraw Cash \n3.Check Balance \n4.Exit\n"))

    match ch:
        case 1:
            print("Deposited Cash")
            damt = int(input("Enter Cash to be Deposited: "))
            deposit(damt)
        case 2:
            print("Withdraw Cash: ")
            wamt = int(input("Enter Cash to be withdraw: "))
            withdraw(wamt)
           
        case 3:
            print("Check Balance: ")
            check_bal()
        case 4:
            print("Exit")
            break
            
        case _ :
            print("Invalid Choice")

    
