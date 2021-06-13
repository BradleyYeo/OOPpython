# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Author:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
        self.books = []

    def write(self, title):
        print(f"{self.name} is working on {title}")

    def publish(self, book):
        self.books.append(book)
        print(f"It is {book.year} and {self.name} has just published {book.title}!")

    def get_biblio(self):
        print(f"Author name {self.name}")
        for book in self.books:
            print(f"{book.title} published in {book.year}")


class Book:
    def __init__(self, title, year, author, price):
        self.title = title
        self.year = year
        self.author = author
        self.price = price
        self.versions = {year: price}

    def reprint(self, year, price):
        self.year = year
        self.price = price
        self.versions[year] = price
        print(f"Reprinting {self.title} from {year} at {price}")

jrr = Author("Tolkien", "JRR.tolkien@gmail.com", "Male")
b1 = Book("Hobbir", 1995, jrr, 100)
jrr.publish(b1)
b1.reprint(2000, 60)
b2 = Book("Lord of the rings", 1995, jrr, 100)
jrr.publish(b2)
jrr.get_biblio()

class Blogger (Author):
    def __init__(self, name, email, gender, posts):
        super().__init__(name, email, gender)
        self.posts = posts



