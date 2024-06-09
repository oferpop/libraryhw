import unittest
import sqlite3
from books import Book
from customers import Customer
from loans import Loan

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        Book.create_table(self.cursor)
        Customer.create_table(self.cursor)
        Loan.create_table(self.cursor)

    def tearDown(self):
        self.conn.close()

    def test_add_book(self):
        book = Book(None, "Book 1", "Author 1", 2021, 1)
        book.save(self.cursor)
        self.conn.commit()
        self.cursor.execute("SELECT * FROM Books WHERE Name = 'Book 1'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_add_customer(self):
        customer = Customer(None, "Customer 1", "City 1", 30)
        customer.save(self.cursor)
        self.conn.commit()
        self.cursor.execute("SELECT * FROM Customers WHERE Name = 'Customer 1'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_add_loan(self):
        book = Book(None, "Book 1", "Author 1", 2021, 1)
        book.save(self.cursor)
        customer = Customer(None, "Customer 1", "City 1", 30)
        customer.save(self.cursor)
        self.conn.commit()

        loan = Loan(1, 1, "2024-06-01", "2024-06-11")
        loan.save(self.cursor)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM Loans WHERE CustID = 1 AND BookID = 1")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
