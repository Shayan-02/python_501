class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # متغیر خصوصی

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


# ایجاد یک حساب بانکی
account = BankAccount(1000)

# واریز و برداشت
account.deposit(500)
account.withdraw(200)

# نمایش موجودی حساب
print("Current Balance:", account.get_balance())

# تلاش برای دسترسی مستقیم به متغیر خصوصی (با شکست مواجه خواهد شد)
# print(account.__balance)  # AttributeError
