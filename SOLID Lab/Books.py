class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def __str__(self):
        return f'This is {self.title}, written by {self.author} in {self.location}.'


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


# harry_potter1 = Book("The Philosopher's stone", "J. K. Rowling", "England")
# harry_potter2 = Book("The Chamber of secrets", "J. K. Rowling", "England")
# harry_potter3 = Book("The prisoner of Azkaban", "J. K. Rowling", "England")
# 
# my_library = Library([harry_potter1, harry_potter2, harry_potter3])
# 
# print(my_library.find_book("The prisoner of Azkaban"))
