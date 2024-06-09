import sqlite3
from enum import Enum, auto

class MenuOptions(Enum):
    ADD_BOOK = auto()
    ADD_CUSTOMER = auto()
    ADD_LOAN = auto()
    DISPLAY_BOOKS = auto()
    DISPLAY_CUSTOMERS = auto()
    DISPLAY_LOANS = auto()
    DELETE_BOOK = auto()
    DELETE_CUSTOMER = auto()
    DELETE_LOAN = auto()
    EXIT = auto()

def create_tables():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            Author TEXT,
            YearPublished INTEGER,
            Type INTEGER
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            Id INTEGER PRIMARY KEY,
            Name TEXT,
            City TEXT,
            Age INTEGER
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Loans (
            CustID INTEGER,
            BookID INTEGER,
            LoanDate TEXT,
            ReturnDate TEXT,
            FOREIGN KEY (CustID) REFERENCES Customers(Id),
            FOREIGN KEY (BookID) REFERENCES Books(Id)
        )
    """)

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return wrapper

@error_handler
def add_book():
    name = input('Book Name? ')
    author = input('Author? ')
    year_published = input('Year Published? ')
    book_type = input('Type (1/2/3)? ')
    cur.execute("INSERT INTO Books (Name, Author, YearPublished, Type) VALUES (?, ?, ?, ?)", 
                (name, author, year_published, book_type))
    con.commit()
    print("Book added successfully.")

@error_handler
def add_customer():
    name = input('Customer Name? ')
    city = input('City? ')
    age = input('Age? ')
    cur.execute("INSERT INTO Customers (Name, City, Age) VALUES (?, ?, ?)", 
                (name, city, age))
    con.commit()
    print("Customer added successfully.")

@error_handler
def add_loan():
    cust_id = input('Customer ID? ')
    book_id = input('Book ID? ')
    loan_date = input('Loan Date (YYYY-MM-DD)? ')
    return_date = input('Return Date (YYYY-MM-DD)? ')
    cur.execute("INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)", 
                (cust_id, book_id, loan_date, return_date))
    con.commit()
    print("Loan added successfully.")

@error_handler
def display_books():
    res = cur.execute("SELECT * FROM Books")
    books = res.fetchall()
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(book)

@error_handler
def display_customers():
    res = cur.execute("SELECT * FROM Customers")
    customers = res.fetchall()
    if not customers:
        print("No customers in the table.")
    else:
        for customer in customers:
            print(customer)

@error_handler
def display_loans():
    res = cur.execute("SELECT * FROM Loans")
    loans = res.fetchall()
    if not loans:
        print("No loans in the table.")
    else:
        for loan in loans:
            print(loan)

@error_handler
def delete_book():
    try:
        book_id = int(input('Book ID? '))
    except ValueError:
        print("Invalid Book ID. Please enter a numeric value.")
        return

    cur.execute("DELETE FROM Books WHERE Id = ?", (book_id,))
    con.commit()
    if cur.rowcount == 0:
        print("No such book found.")
    else:
        print("Book deleted successfully.")

@error_handler
def delete_customer():
    try:
        customer_id = int(input('Customer ID? '))
    except ValueError:
        print("Invalid Customer ID. Please enter a numeric value.")
        return

    cur.execute("DELETE FROM Customers WHERE Id = ?", (customer_id,))
    con.commit()
    if cur.rowcount == 0:
        print("No such customer found.")
    else:
        print("Customer deleted successfully.")

@error_handler
def delete_loan():
    try:
        cust_id = int(input('Customer ID? '))
        book_id = int(input('Book ID? '))
    except ValueError:
        print("Invalid ID. Please enter numeric values for both Customer ID and Book ID.")
        return

    cur.execute("DELETE FROM Loans WHERE CustID = ? AND BookID = ?", (cust_id, book_id))
    con.commit()
    if cur.rowcount == 0:
        print("No such loan found.")
    else:
        print("Loan deleted successfully.")

def menu():
    while True:
        print("\nMenu:")
        for option in MenuOptions:
            print(f"{option.value}. {option.name.replace('_', ' ').title()}")
        choice = input("Choose an option: ")

        try:
            choice = MenuOptions(int(choice))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == MenuOptions.ADD_BOOK:
            add_book()
        elif choice == MenuOptions.ADD_CUSTOMER:
            add_customer()
        elif choice == MenuOptions.ADD_LOAN:
            add_loan()
        elif choice == MenuOptions.DISPLAY_BOOKS:
            display_books()
        elif choice == MenuOptions.DISPLAY_CUSTOMERS:
            display_customers()
        elif choice == MenuOptions.DISPLAY_LOANS:
            display_loans()
        elif choice == MenuOptions.DELETE_BOOK:
            delete_book()
        elif choice == MenuOptions.DELETE_CUSTOMER:
            delete_customer()
        elif choice == MenuOptions.DELETE_LOAN:
            delete_loan()
        elif choice == MenuOptions.EXIT:
            break
        else:
            print("Invalid choice. Please try again.")

con = sqlite3.connect("library.db")
cur = con.cursor()

create_tables()
menu()

con.close()
