import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction 
import z_obj

path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()


if __name__ == "__main__":
    root.customers = BTrees.OOBTree.OOBTree()
    root.customers["Dave"] = z_obj.Customer("Dave")
    d = root.customers["Dave"]
    root.customers["Jone"] = z_obj.Customer("Jone")
    j = root.customers["Jone"]

    print("Create Account:")
    b1 = d.add_account(z_obj.SavingAccount(400,d))
    b2 = j.add_account(z_obj.CheckingAccount(800,j))
    d.printStatus()
    j.printStatus()

    print("\nDeposit 500 to Jone's Saving Account:")
    b2.deposit(500)
    j.printStatus()

    print("WithDraw 200 from Dave's Saving Account:")
    b1.withdraw(200)
    d.printStatus()

    print("Transfer 150 from Jone's Checking Account to Dave's Saving Account:")
    b2.transfer(150, b1)
    d.printStatus()
    j.printStatus()

    transaction.commit()
    connection.close()