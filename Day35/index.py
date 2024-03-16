class Library:
    def __init__(self, name, location, contact):
        self.name = name
        self.location = location
        self.contact = contact
        self.books = []  # List to store book information
        self.staff = {}  # Dictionary to store staff information

    def add_book(self, book):
        self.books.append(book)

    def add_staff(self, staff_id, name, role):
        self.staff[staff_id] = {'name': name, 'role': role}

    def search_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                return book
        return None

    def print_staff_info(self):
        print("\nStaff Information:")
        for staff_id, info in self.staff.items():
            print(f"Staff ID: {staff_id}")
            print(f"Name: {info['name']}")
            print(f"Role: {info['role']}\n")

# Example usage
my_library = Library(name="Central Library", location="City Center", contact="library@example.com")

# Add books
my_library.add_book({'title': 'Python Basics', 'author': 'John Doe', 'genre': 'Programming', 'available': True})
my_library.add_book({'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'available': False})

# Add staff
my_library.add_staff(staff_id='L001', name='Alice Smith', role='Librarian')
my_library.add_staff(staff_id='L002', name='Bob Johnson', role='Assistant Librarian')

# Search for a book
search_title = input("Enter book title to search: ")
found_book = my_library.search_book(search_title)
if found_book:
    print(f"Book found: {found_book['title']} by {found_book['author']}")
else:
    print("Book not found.")

# Print staff information
my_library.print_staff_info()
