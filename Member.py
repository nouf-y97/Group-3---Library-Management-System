class Member:
    def __init__(self, name, member_id):#يتم استدعاؤها تلقائيًا عند إنشاء كائن جديد من الكلاس
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
        print(f"""
                Name: {self.name}
                ID: {self.member_id}
                Borrowed Books: {len(self.borrowed_books)}
                Late Fees: {self._late_fees} SAR
                """)
        
class StudentMember(Member):
    def borrow_limit(self):
        return 3
    
class StaffMember(Member):
    def borrow_limit(self):
        return 10