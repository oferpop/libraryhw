import sqlite3

class Customer:
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                Id INTEGER PRIMARY KEY,
                Name TEXT,
                City TEXT,
                Age INTEGER
            )
        """)

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO Customers (Name, City, Age) VALUES (?, ?, ?)
        """, (self.name, self.city, self.age))
