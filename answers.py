# Activity 1: Class Creation and Inheritance

class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def describe(self): # Example of polymorphism
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}")


class eBook(Book): # Inherits from Book
    def __init__(self, title, author, genre, pages, format):
        super().__init__(title, author, genre, pages) # Call the parent class constructor
        self.format = format


    def describe(self): # Overriding the describe method (polymorphism)
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}, Format: {self.format}")

# Activity 2: Polymorphism Challenge

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")


class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗") # Different implementation for Car


class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️") # Different implementation for Plane


class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing ⛵️") # Different implementation for Boat



# Example Usage
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 310)
ebook1 = eBook("The Martian", "Andy Weir", "Sci-Fi", 384, "EPUB")



book1.describe()
ebook1.describe() # Polymorphism: different output for Book and eBook

book1.borrow()


car1 = Car("My Car")
plane1 = Plane("Jetliner")
boat1 = Boat("Sailboat")



car1.move()      # Output: My Car is driving 🚗
plane1.move()   # Output: Jetliner is flying ✈️
boat1.move()    # Output: Sailboat is sailing ⛵️






