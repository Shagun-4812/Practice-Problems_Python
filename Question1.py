class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        
        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transferred ${amount:.2f} to account {target_account.account_number}")
    
    def __str__(self) -> str:
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, initial_balance: float = 0.0, interest_rate: float = 0.0):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self) -> None:
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Added ${interest:.2f} interest to account {self.account_number}")
    
    def __str__(self) -> str:
        return (f"Savings Account {self.account_number}: "
                f"Balance ${self.balance:.2f}, "
                f"Interest Rate {self.interest_rate}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, initial_balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > (self.balance + self.overdraft_limit):
            raise ValueError("Withdrawal amount exceeds available balance and overdraft limit")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    def __str__(self) -> str:
        return (f"Checking Account {self.account_number}: "
                f"Balance ${self.balance:.2f}, "
                f"Overdraft Limit ${self.overdraft_limit:.2f}")


# Testing the classes
if __name__ == "__main__":
    print("=== Testing BankAccount ===")
    acc1 = BankAccount("1001", 1000)
    acc2 = BankAccount("1002", 500)
    print(acc1)
    print(acc2)
    
    acc1.deposit(200)
    acc1.withdraw(50)
    acc1.transfer(300, acc2)
    print(acc1)
    print(acc2)
    
    print("\n=== Testing SavingsAccount ===")
    savings = SavingsAccount("2001", 1000, 5.0)  # 5% interest
    print(savings)
    savings.add_interest()
    print(savings)
    
    print("\n=== Testing CheckingAccount ===")
    checking = CheckingAccount("3001", 500, 200)  # $200 overdraft
    print(checking)
    checking.withdraw(600)  # Should work (500 + 200 overdraft)
    print(checking)
    try:
        checking.withdraw(200)  # Should fail (balance is -100, overdraft is 200, but 200 > 100 remaining)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Testing Transfer Between Different Account Types ===")
    savings.transfer(200, checking)
    print(savings)
    print(checking)
    
    
    
    