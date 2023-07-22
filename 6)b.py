class Account:
    def __init__(self,bal,amt):
        self.bal = bal
        self.amt = amt
        self.bal += amt
    def deposit(self,amt):
        if amt<0:
            raise ValueError("Amount cannot be negative")
        self.bal += amt
        print(f"Amt deposited, total bal {self.bal}")
    def withdraw(self,amt):
        if amt<0:
            raise ValueError("Amount cannot be negative")
        if amt>self.bal:
            raise ValueError("withdrawl amount exceeded bal")
        self.bal -=amt
        print(f"Amt withdrawn, total bal {self.bal}")

bal = 1000
amt = 500

acc = Account(bal,amt)
try:
    acc.deposit(100)
except ValueError as e:
    print(str(e))

try:
    acc.deposit(-100)
except ValueError as e:
    print(str(e))

try:
    acc.withdraw(-2000)
except ValueError as e:
    print(str(e))

try:
    acc.withdraw(2000)
except ValueError as e:
    print(str(e))
    
try:
    acc.withdraw(200)
except ValueError as e:
    print(str(e))




