class Book:
    def __init__(self, title, author, year, isbn, genre):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.is_borrowed = False

   
    def info(self):
        return (self.title, self.author, self.year)

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"