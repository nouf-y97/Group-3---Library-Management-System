from book import *
from Member import *

class Library:
    def __init__(self):
        self.books = []
        self.members = {}
        self.genres = set()
#1
    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")       
        while True:
            year = input("Year: ")
            try:
                year = int(year)
                break
            except ValueError:
                print("Invalid year")
                
        isbn = input("ISBN: ")
        genre = input("Genre: ") 

        book = Book(title , author , year ,isbn , genre) 

        self.books.append(book)
        self.genres.add(genre)
        book.display()
        return print("✓ Book added!")

# 2
    def register_member(self):
        name = input("Name: ")

        while True:
            member_id = input("Member ID: ")
            try:
                member_id = int(member_id)
                break
            except ValueError:
                print("Invalid ID")
                

        if member_id in self.members:                       
                print("Member already exists")
                return

        while True:
            member_type = input("Type (student/staff): ")
            match member_type.lower():
                case "student":
                    new_member = StudentMember(name, member_id) 
                    print("✓ Student member registered!")
                    break

                case "staff":
                    new_member = StaffMember(name, member_id) 
                    print("✓ Staff member registered!")  
                    break
                case _:
                    print("Please enter valid input")
                    continue

        self.members[member_id] = new_member              

# 3
    def borrow_book(self):  
        while True:
            try:
                member_id = int(input("Member ID: "))
                break
            except ValueError:
                print("Invalid ID, Try again")
                

        if member_id not in self.members:
            print("Member not found")
            return

        title = input("Book title: ")

        book_found = None

        for book in self.books:
            if book.title.lower() == title.lower():
                book_found = book
                break

        if not book_found:
            print("Book not found")
            return

        if book_found.is_borrowed:
            print("Book already borrowed")
            return

        member = self.members[member_id]

        if len(member.borrowed_books) >= member.borrow_limit():
            print("Limit reached")
            return
        book_found.is_borrowed = True
        member.borrowed_books.append(book_found)

        print(f"✓ {member.name} borrowed {book_found.title}")

   # 4
    def return_book(self):
        try:
            member_id = int(input("Enter member ID: "))
            days_late = int(input("Days late: "))
        except ValueError:
            print("Invalid input")
            return

        title = input("Enter book title: ")

        if member_id not in self.members:
            print("Member not found")
            return

        member = self.members[member_id]

        for book in member.borrowed_books:
            if book.title.lower() == title.lower():
                member.borrowed_books.remove(book)
                book.is_borrowed = False

                fee = days_late * 2
                member.add_fee(fee)

                print(
                    f"Returned. Late fee: {fee} SAR. "
                    f"Total fees on account: {member.get_fees()} SAR."
                )
                return
        print("Book not found in member's borrowed books")


#5 
    def search(self):               
        keyword = input("Enter keyword: ")

        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display()
                break             
            else:
                print("No books match that keyword")
               

#6
    def show_all(self):

        choice = input("Show (books/members): ").lower()

        match choice:
            case "books":
                for book in self.books:
                    book.display()

            case "members":
                for member in self.members.values():
                    member.display()
            case _:
                print("Invalid choice")

#7
    def show_stats(self):
        length_of_books = len(self.books)
        length_of_members = len(self.members)
        length_of_genres = len(self.genres)
        genre_names = self.genres
        count = 0
        for i in self.books:
            if i.is_borrowed:
                count += 1
        
        total_late_fees = sum(m.get_fees() for m in self.members.values())

        print(f"""Total Books: {length_of_books}\nTotal Members: {length_of_members}\nCurrently Borrowed: {count}
Unique Genres: {length_of_genres} , {genre_names}\nTotal Late Fees: {total_late_fees}""")
    


lib = Library()

lib.books.append(Book("Clean Code", "Robert Martin", 2008, "111-1111", "Programming"))
lib.books.append(Book("Python Basics", "John Smith", 2021, "222-2222", "Programming"))
lib.books.append(Book("Data Science", "Ahmed Ali", 2020, "333-3333", "Technology"))
lib.books.append(Book("The Alchemist", "Paulo Coelho", 1988, "444-4444", "Novel"))
lib.books.append(Book("Atomic Habits", "James Clear", 2018, "555-5555", "Self Development"))

for b in lib.books:

    lib.genres.add(b.genre)

lib.members[101] = StudentMember("Dalal", 101)
lib.members[102] = StudentMember("Afnan", 102)
lib.members[103] = StudentMember("Nouf", 103)
lib.members[201] = StaffMember("Ahmed", 201)
lib.members[202] = StaffMember("Khalid", 202)
lib.members[203] = StaffMember("Reem", 203)

while True:
    print("\n=== LIBRARY ===")
    print("1.Add book  2.Register  3.Borrow  4.Return")
    print("5.Search    6.Show all  7.Stats   8.Exit")
    choice = input("> ")
    try:
        match choice:
            case "1": lib.add_book()
            case "2": lib.register_member()
            case "3": lib.borrow_book()
            case "4": lib.return_book()
            case "5": lib.search()
            case "6": lib.show_all()
            case "7": lib.show_stats()              
            case "8": print("Goodbye!"); break
            case _:   print("Invalid choice")
    except Exception as e:
        print(f"Error: {e}")