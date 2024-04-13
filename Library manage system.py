# Library management system
class Book:
    def __init__(self, title, author, isbn, genre):  # cnst
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True  # initially the book is available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the library.")

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search_book_by_auther(self, author):
        author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                author_books.append(book)
            return author_books

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available_Books: ")
            for book in available_books:
                print(f" - {book}")
        else:
            print("No books available!")


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_books(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"This book is not available for borrowing. ")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book_available = True
            print(f"{self.name} has returned '{book.title}'")
        else:
            print("You don't have borrowed this Book")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books: ")
            for book in self.borrowed_books:
                print(f" - {book}")
        else:
            print("You have not borrowed any books.")


class Transaction:
    @staticmethod
    def display_transaction_history(member):
        print(f"The transaction history for {member.name}")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"{member.name} borrowed '{book.title}'")
        else:
            print(f"{member.name} has not borrowed any books.")


library = Library()

book1 = Book("Born of Bangladesh", "Johir raihan", "1234567890", "History")
book2 = Book("The Jungle Book", "Rudyard Kipling", "1234567891", "adventure, fiction")
book3 = Book("Sonali dukkhu", "Sunil Gangapaddhay", "1234567892", "romance, drama")
book4 = Book("Gitanjali", "Rabindranath Tagaore", "1234567893", "poem collection/poetry")
book5 = Book("Harry potter", "J. K. Rowling", "1234567894", "fiction, adventure")
book6 = Book("Lord of the Rings", "Tolkien", "1234567895", "fiction, adventure")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

member1 = Member("Ashish", "320CSE")
member2 = Member("Rabbi", "319CSE")
member3 = Member("Rana", "321CSE")
member4 = Member("Jabed", "322CSE")
member5 = Member("Nusrat", "323CSE")
member6 = Member("Shaminaj", "324CSE")
member7 = Member("Miskat", "325CSE")
member8 = Member("Sami", "326CSE")

member1.borrow_books(book6)
member2.borrow_books(book3)
member3.borrow_books(book5)
member4.borrow_books(book5)
member5.borrow_books(book2)
member6.borrow_books(book4)

Transaction.display_transaction_history(member1)
# this dataset made by Ashish kumar
