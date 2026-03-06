class BankAccount:

    # Class attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        BankAccount.total_bank_balance += amount

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
        else:
            print("Insufficient balance")

    # Display account info
    def display_account_info(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    # Class method to show bank summary
    @classmethod
    def display_bank_summary(cls):
        print("Bank Name:", cls.bank_name)
        print("Total Accounts:", cls.total_accounts)
        print("Total Bank Balance:", cls.total_bank_balance)