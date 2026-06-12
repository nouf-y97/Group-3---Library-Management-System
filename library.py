# 2
    def register_member(self):
        name = input("Name: ")

        try:
            member_id = int(input("Member ID: "))
        except ValueError:
            print("Invalid ID")
            return

        if member_id in self.members:                       
            print("Member already exists")
            return

        member_type = input("Type (student/staff): ")

        match member_type.lower():
            case "student":
                new_member = StudentMember(name, member_id) 
                print("✓ Student member registered!")

            case "staff":
                new_member = StaffMember(name, member_id) 
                print("✓ Staff member registered!")  

            case _:
                print("Invalid type")
                return

        self.members[member_id] = new_member              

# 3
    def borrow_book(self):    
        try:
            member_id = int(input("Member ID: "))
        except ValueError:
            print("Invalid ID")
            return

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
            days_late = int(input("Days late: ")
        except ValueError:
            pr  #int("Invalid input")
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

        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display()
                found = True

        if not found:
            print("No books match that keyword")
