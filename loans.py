import sqlite3
from books import Book

class Loan:
    def __init__(self, cust_id, book_id, loan_date, return_date):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    @staticmethod
    def create_table(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Loans (
                CustID INTEGER,
                BookID INTEGER,
                LoanDate TEXT,
                ReturnDate TEXT,
                FOREIGN KEY (CustID) REFERENCES Customers(Id),
                FOREIGN KEY (BookID) REFERENCES Books(Id)
            )
        """)

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)
        """, (self.cust_id, self.book_id, self.loan_date, self.return_date))
