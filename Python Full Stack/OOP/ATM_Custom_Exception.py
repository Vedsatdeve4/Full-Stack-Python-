
Balance = 0

class Atm(BaseException):

    def __init__(self,msg):
        self.msg = msg
try:
    withdraw = int(input("Enter the amount to withdraw: "))
    totalbalance = 1000

    if totalbalance < withdraw:
        raise Atm("Insufficient Money")

except (Atm, ValueError):
    print("Please enter correct value")
    
else:
    totalbalance -=  withdraw
    print(totalbalance)
