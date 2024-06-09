import sqlite3

class Book:
    def __init__(self, id, name, author, year_published, book_type):
        self.id = id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                Id INTEGER PRIMARY KEY,
                Name TEXT,
                Author TEXT,
                YearPublished INTEGER,
                Type INTEGER
            )
        """)

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO Books (Name, Author, YearPublished, Type) VALUES (?, ?, ?, ?)
        """, (self.name, self.author, self.year_published, self.book_type))

    @staticmethod
    def get_max_loan_days(book_type):
        if book_type == 1:
            return 10
        elif book_type == 2:
            return 5
        elif book_type == 3:
            return 2
        else:
            raise ValueError("Invalid book type")
