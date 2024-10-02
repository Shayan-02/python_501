from random import randrange
class BankAccount:
    all_account_number = set()

    def __init__(self, name):
        while True:
            if (account_number := randrange(10000, 1000000) not in BankAccount.all_account_number):
                BankAccount.all_account_number.add(account_number)
                break
        self.name = name
        self.balance = 0
        self.account_number = account_number

    def display(self):
        print(40 * "-")
        print(f"hi, {self.name}\nyour current balance: {self.balance}")
        print(40 * "-")

    def deposit(self):
        amount = int(input("enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self):
        amount = int(input("enter amount to withdraw: "))
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
        self.display()


def main():
    ac1 = BankAccount("ali")
    print(ac1.account_number)
    ac1.display()
    while True:
        choice = int(input("enter 1 to "))
if __name__ == "__main__":
    main()
