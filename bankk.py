# Simple Bank Account Management System

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance")
        elif amount <= 0:
            print("❌ Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ₹{amount}")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")


# -------- Main Program --------
print("🏦 Welcome to Simple Bank System 🏦")

name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("👋 Thank you for using the bank system")
        break

    else:
        print("❌ Invalid choice, try again")
