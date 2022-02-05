class bankAccount:
    def __init__(self,name,accountNo,Accounttype,balance):
        self.name = name
        self.accountNo = accountNo
        self.Accounttype = Accounttype
        self.balance = balance
    def deposit(self,a):
        self.balance = self.balance + a
        return self.balance
    def withdraw(self,b):
        self.balance = self.balance - b
        return self.balance
sara =bankAccount("sona",123456,"AC",15000)  
print(sara.deposit(1000))
print(sara.withdraw(500))
