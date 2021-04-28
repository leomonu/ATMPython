class Atm(object):
    def __init__(self,cardNumber,pinCode):
        self.cardNumber = cardNumber
        self.pinCode = pinCode
        

    def cashWithDrawal(self):
        print("Cash Withdrawed")

    def balanceEnqiry(self):
        print("Balance Enquired")

    def cashDeposit(self):
        print("Cash Deposited")

    
Josh = Atm(5440345727,1234)

print("Pin No. is "+str(Josh.pinCode))

print("Card No. is "+str(Josh.cardNumber))

    
    
Josh.cashWithDrawal()

Josh.balanceEnqiry()

Josh.cashDeposit()