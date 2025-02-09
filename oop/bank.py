from faker import Faker
import random
from datetime import datetime

faker = Faker('en_IN')

class Customer:
    def __init__(self, name, email, address, phone):
        self.id = random.randint(1000, 9999)
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __repr__(self):
        return f'Customer({self.id}, {self.name}, {self.email})'

class Account:
    def __init__(self, customer, balance=0.0):
        self.id = random.randint(100000, 999999)
        self.customer = customer
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(self.id, amount, 'Deposit'))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self.id, amount, 'Withdrawal'))
        else:
            print("Insufficient funds!")

    def __repr__(self):
        return f'Account({self.id}, Balance: {self.balance})'

class Transaction:
    def __init__(self, account_id, amount, transaction_type):
        self.id = random.randint(10000000, 99999999)
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_date = datetime.now()

    def __repr__(self):
        return f'Transaction({self.id}, {self.transaction_type}, {self.amount}, {self.transaction_date})'

# Example Usage
if __name__ == "__main__":
    # Generate fake customer data
    customer = Customer(name=faker.name(), email=faker.email(), address=faker.address(), phone=faker.phone_number())
    print(customer)
    
    # Create a new account for the customer
    account = Account(customer=customer)
    customer.add_account(account)
    print(account)

    # Perform some transactions
    account.deposit(1000)
    account.withdraw(500)
    account.withdraw(100)
    account.withdraw(100000)

    # Print account details and transactions
    print(account)
    for transaction in account.transactions:
        print(transaction)
