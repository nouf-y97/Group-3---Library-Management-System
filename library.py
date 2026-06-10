
from book import *
from Member import *

# class Library
#      Attributes:  books=[], members={}, genres=set()
#      Methods:     add_book, register_member, borrow_book, return_book,
#                   search, show_stats



class Library:
    def __init__(self):
        self.books = []
        self.members = {}
        self.geners = set()

    def add_book(self):
        title = input("Title: ")
        author = input("Ahuthor: ")
        year = input("Year: ")
        try:
            year = int(year)
        except ValueError:
            print("Invalid year")
            return
        isbn = input("ISBN: ")
        genre = input("Genre: ") 

        book = Book(title , author , year ,isbn , genre) # عدليه كاوبجكت بوك 

        self.books.append(book)
        self.geners.add(genre)
        #self.books.display()
        return print("✓ Book added!")


    def register_member():
        pass

    def borrow_book():
        pass

    def return_book():
        pass

    def search():
        pass

    def show_stats():
        pass



lib = Library()
lin = Book()
lib.add_book()
lin.display()


