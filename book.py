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
 
    # def display(self): 
    #     status = "Borrowed" if self.is_borrowed else "Available" 
 
    #     return f"{self.title} by {self.author} ({self.year}) - {status}" 
 
    def display(self): 
        status = "Borrowed" if self.is_borrowed else "Available" 
        return f""" 
        Title : {self.title} 
        Author: {self.author} 
        Year  : {self.year} 
        ISBN  : {self.isbn} 
        Genre : {self.genre} 
        Status: {status}
        """