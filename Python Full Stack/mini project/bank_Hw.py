balance = 0

def check_balance():
    print("\nCurrent Balance is: ",balance)

def deposit(amt):
    global balance
    balance += amt
    print("\nDeposited money: " , amt)

def withdraw(amt):
    global balance
    if amt <= balance:
        balance -= amt
        print("\nWithdraw money: " , amt)
    else:
        print("\nInsufficient Balance")

while True:
    ch = int(input("Enter your choice:\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit "))

    if ch == 1:
        des = int(input("Enter money to be Deposited: "))
        deposit(des)
    elif ch == 2:
        wth = int(input("Enter money to be Withdraw: "))
        withdraw(wth)
    elif ch == 3:
        check_balance()
    elif ch == 4:
        print("Exit")
        break
    else:
        print("\nInvalid choice")
