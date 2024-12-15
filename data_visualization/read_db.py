# Import SQLite library
import sqlite3
# Assign the database name

db_path = r'../flask_daily_report/app/reports.db'

conn = sqlite3.connect(db_path )

c = conn.cursor()