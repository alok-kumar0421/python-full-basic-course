#_ protected ->can access from anywhere
#__ private ->can't access only from same class ||getter & setter
class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):  #getter
        return self.__balance
    
    def set_balance(self,new_balance): #setter
        self.__balance=new_balance

    def get_info(self):
        print(f"name is {self.name} & balance is {self.balance}")

ac1=bank_account("Alok",100000000000)

ac1.set_balance(20000000000000000)

print(ac1.name,ac1.get_balance())