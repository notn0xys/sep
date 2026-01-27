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
    for customers in root.customers:
        obj = root.customers[customers]
        obj.printStatus()
        print("-----")
        idx = 0
        while obj.getAccounts(idx) is not None:
            acc = obj.getAccounts(idx)
            acc.printStatus()
            acc.printBankTransaction()
            idx += 1 
