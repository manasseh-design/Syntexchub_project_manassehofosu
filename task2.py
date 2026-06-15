import json
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_issued = False #False means the book is available, True means the book is issued
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title, author, ISBN):
        if ISBN in self.books:
            print(f"Book with ISBN {ISBN} already exists.")
            return
        self.books[ISBN] = Book(title, author, ISBN)
        print(f"Book '{title}' added successfully.")
    def search_book(self, title):
            found = []
            for book in self.books.values():
                if title.lower() in book.title.lower():
                    found.append(book)
            if not found:
                print(f"No books found with title containing '{title}'.")
                return
            for book in found:
                status = "Issued" if book.is_issued else "Available"
                print(f"Title: {book.title} | Author: {book.author} | ISBN: {book.ISBN} | Status: {status}")
    def issue_book(self, ISBN):
        if ISBN not in self.books:
            print(f"Book with ISBN {ISBN} not found.")
            return
        elif self.books[ISBN].is_issued:
            print(f"Book with ISBN {ISBN} is already issued.")
            return
        else:
            self.books[ISBN].is_issued = True
            print(f"Book with ISBN {ISBN} issued successfully.")  
    def return_book(self, ISBN):
        if ISBN not in self.books:
            print(f"Book with ISBN {ISBN} not found.")
            return
        elif not self.books[ISBN].is_issued:
            print(f"Book with ISBN {ISBN} is not issued.")
            return
        else:
            self.books[ISBN].is_issued = False
            print(f"Book with ISBN {ISBN} returned successfully.")
    def show_report(self):
       total_books = len(self.books)
       issued_books = sum(1 for book in self.books.values() if book.is_issued)
       available_books = total_books - issued_books 
       print(f"Total Books: {total_books}")  
       print(f"Issued Books: {issued_books}")  
       print(f"Available Books: {available_books}")  
    def save_to_file(self, filename="library.json"):
        data = {}
        for isbn, book in self.books.items():
            data[isbn] = {
                "title": book.title,
                "author": book.author,
                "ISBN": book.ISBN,
                "is_issued": book.is_issued
            }
        with open(filename, "w") as file:
                    json.dump(data, file)
        print("Data saved to file successfully.")
    def load_from_file(self, filename="library.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for isbn, info in data.items():
                    book = Book(info["title"], info["author"], info["ISBN"])
                    book.is_issued = info["is_issued"]
                    self.books[isbn] = book
            print("Data loaded from file successfully.")
        except Exception as e:
            print(f"Error loading data from file: {e}")
    
def main():
        library = Library()
        library.load_from_file()
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Show Report")
            print("6. Save Data")
            print("7. Load Data")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                ISBN = input("Enter book ISBN: ")
                library.add_book(title, author, ISBN)
            elif choice == "2":
                title = input("Enter book title to search: ")
                library.search_book(title)
            elif choice == "3":
                ISBN = input("Enter book ISBN to issue: ")
                library.issue_book(ISBN)
            elif choice == "4":
                ISBN = input("Enter book ISBN to return: ")
                library.return_book(ISBN)
            elif choice == "5":
                library.show_report()
            elif choice == "6":
                library.save_to_file()
            elif choice == "7":
                library.load_from_file()
            elif choice == "8":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

main()