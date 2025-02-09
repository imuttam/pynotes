import psycopg2
from psycopg2 import sql
from faker import Faker
from datetime import datetime
import random

# Initialize Faker
faker = Faker()

# Database connection setup
conn = psycopg2.connect(
    dbname="bank_db", 
    user="your_username", 
    password="your_password", 
    host="localhost", 
    port="5432"
)
cursor = conn.cursor()

# Create tables
def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            address VARCHAR(200) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL REFERENCES customers(id),
            balance FLOAT DEFAULT 0.0
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            account_id INTEGER NOT NULL REFERENCES accounts(id),
            amount FLOAT NOT NULL,
            transaction_type VARCHAR(50) NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()

# Define Classes
class Customer:
    def __init__(self, name, email, address, phone):
        self.id = self.add_customer(name, email, address, phone)
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    @staticmethod
    def add_customer(name, email, address, phone):
        cursor.execute("""
            INSERT INTO customers (name, email, address, phone)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """, (name, email, address, phone))
        conn.commit()
        return cursor.fetchone()[0]

    def __repr__(self):
        return f'Customer({self.id}, {self.name}, {self.email})'

class Account:
    def __init__(self, customer_id, balance=0.0):
        self.id = self.add_account(customer_id, balance)
        self.customer_id = customer_id
        self.balance = balance

    @staticmethod
    def add_account(customer_id, balance):
        cursor.execute("""
            INSERT INTO accounts (customer_id, balance)
            VALUES (%s, %s) RETURNING id;
        """, (customer_id, balance))
        conn.commit()
        return cursor.fetchone()[0]

    def deposit(self, amount):
        self.balance += amount
        cursor.execute("""
            UPDATE accounts SET balance = %s WHERE id = %s;
        """, (self.balance, self.id))
        cursor.execute("""
            INSERT INTO transactions (account_id, amount, transaction_type)
            VALUES (%s, %s, %s);
        """, (self.id, amount, 'Deposit'))
        conn.commit()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            cursor.execute("""
                UPDATE accounts SET balance = %s WHERE id = %s;
            """, (self.balance, self.id))
            cursor.execute("""
                INSERT INTO transactions (account_id, amount, transaction_type)
                VALUES (%s, %s, %s);
            """, (self.id, amount, 'Withdrawal'))
            conn.commit()
        else:
            print("Insufficient funds!")

    def __repr__(self):
        return f'Account({self.id}, Balance: {self.balance})'

class Transaction:
    def __init__(self, account_id, amount, transaction_type):
        self.id = self.add_transaction(account_id, amount, transaction_type)
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_date = datetime.now()

    @staticmethod
    def add_transaction(account_id, amount, transaction_type):
        cursor.execute("""
            INSERT INTO transactions (account_id, amount, transaction_type)
            VALUES (%s, %s, %s) RETURNING id;
        """, (account_id, amount, transaction_type))
        conn.commit()
        return cursor.fetchone()[0]

    def __repr__(self):
        return f'Transaction({self.id}, {self.transaction_type}, {self.amount}, {self.transaction_date})'

# Example Usage
if __name__ == "__main__":
    create_tables()
    
    # Generate fake customer data
    customer = Customer(name=faker.name(), email=faker.email(), address=faker.address(), phone=faker.phone_number())
    print(customer)
    
    # Create a new account for the customer
    account = Account(customer_id=customer.id)
    print(account)

    # Perform some transactions
    account.deposit(1000)
    account.withdraw(500)
    account.withdraw(100)

    # Print account details and transactions
    print(account)
    cursor.execute("SELECT * FROM transactions WHERE account_id = %s", (account.id,))
    transactions = cursor.fetchall()
    for transaction in transactions:
        print(transaction)

    # Close the cursor and connection
    cursor.close()
    conn.close()
