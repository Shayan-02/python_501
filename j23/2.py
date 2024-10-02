class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Encapsulation with private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Current balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        return f"Current balance: {self.__balance}"


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, balance=0):
        if owner not in self.accounts:
            self.accounts[owner] = Account(owner, balance)
            print(f"Account created for {owner}.")
        else:
            print(f"Account for {owner} already exists.")

    def access_account(self, owner):
        if owner in self.accounts:
            return self.accounts[owner]
        else:
            print(f"No account found for {owner}.")
            return None


# Testing the ATM program
atm = ATM()
atm.create_account("Alice", 100)
atm.create_account("Bob", 50)

alice_account = atm.access_account("Alice")
if alice_account:
    alice_account.deposit(50)
    alice_account.withdraw(30)
    print(alice_account.check_balance())

bob_account = atm.access_account("Bob")
if bob_account:
    bob_account.withdraw(100)  # Insufficient balance test
    print(bob_account.check_balance())
