class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self._late_fees = 0

    def borrow_limit(self):
        return 0

    def get_fees(self):
        return self._late_fees

    def add_fee(self, amount):
        self._late_fees += amount

    def display(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {len(self.borrowed_books)}")
        print(f"Late Fees: {self._late_fees} SAR")