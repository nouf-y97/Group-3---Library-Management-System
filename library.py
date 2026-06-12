
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
