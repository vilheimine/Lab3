"""
File: bank_system.py
This module defines both the SavingsAccount and Bank classes.
"""
import pickle
import random

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """If the amount is valid, subtract it
        from the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __lt__(self, other):
        """Returns True if this account's name is less than the other's."""
        if not isinstance(other, SavingsAccount):
            return NotImplemented
        return self.name < other.name

    def __eq__(self, other):
        """Returns True if this account's name equals the other's."""
        if not isinstance(other, SavingsAccount):
            return NotImplemented
        return self.name == other.name

    def __le__(self, other):
        """Returns True if this account's name is less than or equal to the other's."""
        if not isinstance(other, SavingsAccount):
            return NotImplemented
        return self.name <= other.name


class Bank:
    """This class represents a bank as a collection of savings accounts.
    An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank with accounts ordered by name."""
        # Convert dictionary values to a list and sort based on account name
        sorted_accounts = sorted(self.accounts.values())
        # Join the string representations with newlines
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or returns None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        return sorted(self.accounts.keys())

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()


# Functions for testing
       
def createBank(numAccounts = 1):
    """Returns a new bank with the given number of 
    accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number = 10, fileName = None):
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""
    testAccount()
    
    # Create a bank and add accounts
    bank = createBank(number)
    print("\nCreated bank with", number, "accounts:")
    print(bank)

if __name__ == "__main__":
    main()
