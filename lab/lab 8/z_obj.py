import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import transaction

path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

class Customer(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return f"Customer: {self.name}"
    def add_account(self, account):
        self.accounts.append(account)
        return account
    def getAccounts(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    def printStatus(self):
        print(self.__str__())
        for acc in self.accounts:
            print("", end="      ")
            acc.printStatus()

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner

    @abstractmethod
    def __str__(self):
        return NotImplementedError("Subclasses must implement __str__ method")
    @abstractmethod
    def accountDetails(self):
        return NotImplementedError("Subclasses must implement accountDetails method")
    @abstractmethod
    def deposit(self, amount):
        return NotImplementedError("Subclasses must implement deposit method")
    def getBalance(self):
        return self.balance
    def printStatus(self):
        print(self.__str__())
        self.accountDetails()
    def printTransaction(self):
        print(f" {self.amount}, New Balance: {self.getBalance()}")
    @abstractmethod
    def transfer(self, amount, target_account):
        return NotImplementedError("Subclasses must implement transfer method")
    @abstractmethod
    def withdraw(self, amount):
        return NotImplementedError("Subclasses must implement withdraw method")
    def transferIn(self, amount, source_account):
        source_account.withdraw(amount)
        self.deposit(amount)

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interest = 0.0):
        super().__init__(balance, owner)
        self.interest = interest

    def __str__(self):
        return f"Saving Account - Balance: {self.balance}, Interest: {self.interest}"
    def accountDetails(self):
        print(f" This is a saving account with interest rate: {self.interest}%")
    def deposit(self, amount):
        self.balance += amount
        self.amount = amount
        self.printTransaction()
        transaction.commit()
    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.amount = amount
            self.printTransaction()
            transaction.commit()
            return True
        else:
            print(" Insufficient funds for withdrawal.")
            return False

class CheckingAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, overdraw_limit = 0.0):
        super().__init__(balance, owner)
        self.overdraw_limit = overdraw_limit

    def __str__(self):
        return f"Checking Account - Balance: {self.balance}, Overdraw Limit: {self.overdraw_limit}"
    def accountDetails(self):
        print(f" This is a checking account with overdraw limit: {self.overdraw_limit}")
    def deposit(self, amount):
        self.balance += amount
        self.amount = amount
        self.printTransaction()
        transaction.commit()
    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraw_limit:
            self.balance -= amount
            self.amount = amount
            self.printTransaction()
            transaction.commit()
            return True
        else:
            print(" Exceeds overdraw limit.")
            return False