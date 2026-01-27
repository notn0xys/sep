import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction 
import z_obj2

path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
    # Create customers
    root.customers = BTrees.OOBTree.OOBTree()
    root.customers["Dave"] = z_obj2.Customer("Dave")
    d = root.customers["Dave"]
    root.customers["Jone"] = z_obj2.Customer("Jone")
    j = root.customers["Jone"]

    print("Create Accounts:")
    # Create accounts with initial balance 0
    b1 = d.add_account(z_obj2.SavingAccount(0, d, 2.5))
    b2 = j.add_account(z_obj2.CheckingAccount(0, j, 100))
    
    print("\nPerforming transactions for Dave's Saving Account:")
    print("Deposit 400:")
    b1.deposit(400)
    
    print("\nDeposit 50:")
    b1.deposit(50)
    
    print("\nWithdraw 25:")
    b1.withdraw(25)
    
    print("\nPerforming transactions for Jone's Checking Account:")
    print("Deposit 800:")
    b2.deposit(800)
    
    print("\nWithdraw 150:")
    b2.withdraw(150)
    
    print("\nWithdraw 50:")
    b2.withdraw(50)
    
    print("\n" + "="*50)
    print("Final Status:")
    print("="*50)
    d.printStatus()
    print("\nDave's Account Transactions:")
    b1.printBankTransaction()
    
    print("\n" + "-"*50)
    j.printStatus()
    print("\nJone's Account Transactions:")
    b2.printBankTransaction()
