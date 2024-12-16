import sqlite3
from faker import Faker
import random

# Initialize Faker for generating fake data
fakes = Faker('en_IN')

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ems.db')
cur = conn.cursor()

def create_table():
    """Creates the employee table if it doesn't already exist."""
    cur.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            company TEXT,
            salary INTEGER,
            hire_date TEXT,
            score INTEGER
        );
    ''')
    print('Table created successfully!')

def insert_data():
    """Inserts a single row of fake data into the employee table."""
    # Generate fake data
    name = fakes.name()
    email = fakes.email()
    company = fakes.company()
    salary = random.randint(40000, 100000)
    hire_date = fakes.date()
    score = random.randint(5, 9)

    # Use parameterized query to safely insert data
    query = """
        INSERT INTO employee (name, email, company, salary, hire_date, score) 
        VALUES (?, ?, ?, ?, ?, ?);
    """
    cur.execute(query, (name, email, company, salary, hire_date, score))
    conn.commit()
    print(f'Inserted data: {name}, {email}, {company}, {salary}, {hire_date}, {score}')

def insert_multiple_data(n):
    """Inserts multiple rows of fake data into the employee table."""
    for _ in range(n):
        insert_data()


def show_data():
    query = """SELECT * FROM employee;"""
    cur.execute(query)
    data = cur.fetchall()
    return data

# if __name__ == "__main__":
    # create_table()
    # insert_multiple_data(10)  # Example: Insert 10 rows of data
    # conn.close()
    # print("Data insertion complete and database connection closed.")

# insert_multiple_data(90)
data = show_data()
for row in data:
    print(row)