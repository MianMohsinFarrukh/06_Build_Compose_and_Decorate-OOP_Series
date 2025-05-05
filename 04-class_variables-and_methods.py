# 4. Class Variables and Class Methods :

# Assignment:

# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "by_default" 

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable


    @classmethod
    def change_bank_name(cls, name):  # method       
        cls.bank_name = name


    def display_bank_name(self):      # Instance method      
        print(f"Account Holder : {self.account_holder}\nBank: {self.bank_name}\n")

account1 = Bank("Asif")
account2 = Bank("kashif")
account3 = Bank("faraz")


account1.display_bank_name()  
account2.display_bank_name()  
account3.display_bank_name()  