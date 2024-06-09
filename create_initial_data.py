import sqlite3
from books import Book
from customers import Customer
from loans import Loan

def create_initial_data(cursor):
    books = [
        Book(None, "Book 1", "Author 1", 2021, 1),
        Book(None, "Book 2", "Author 2", 2020, 2),
        Book(None, "Book 3", "Author 3", 2019, 3),
        Book(None, "Book 4", "Author 4", 2018, 1),
    ]

    customers = [
        Customer(None, "Customer 1", "City 1", 30),
        Customer(None, "Customer 2", "City 2", 25),
        Customer(None, "Customer 3", "City 3", 40),
        Customer(None, "Customer 4", "City 4", 35),
    ]

    loans = [
        Loan(1, 1, "2024-06-01", "2024-06-11"),
        Loan(2, 2, "2024-06-02", "2024-06-07"),
    ]

    for book in books:
        book.save(cursor)
    
    for customer in customers:
        customer.save(cursor)
    
    for loan in loans:
        loan.save(cursor)

if __name__ == '__main__':
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    Book.create_table(cursor)
    Customer.create_table(cursor)
    Loan.create_table(cursor)

    create_initial_data(cursor)

    conn.commit()
    conn.close()
