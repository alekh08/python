class ATMMachine:
    def __init__(self, pin, balance=0):
        # Initialize ATM with a pin, balance, and an empty transaction history
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        # Show current balance
        print(f"Current balance: ${self.balance}")
        self.transaction_history.append("Balance inquiry")
    
    def deposit_cash(self, amount):
        # Add the deposit amount to balance
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.transaction_history.append(f"Deposited: ${amount}")
        else:
            print("Invalid amount. Deposit amount must be greater than zero.")
    
    def withdraw_cash(self, amount):
        # Deduct the withdrawal amount from balance if funds are sufficient
        if amount <= 0:
            print("Invalid amount. Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew: ${amount}")
    
    def change_pin(self, old_pin, new_pin):
        # Change the pin if old pin matches the current one
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect PIN. PIN change failed.")
    
    def view_transaction_history(self):
        # Display the transaction history
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in
