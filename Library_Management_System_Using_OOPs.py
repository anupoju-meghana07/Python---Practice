# ============================================================
# Library Management System Using OOPs
# Based on the structure of the University Management System
# ============================================================

# ---------------- Base Class ---------------- #

class Person:
    library_name = "Codegnan Central Library"   # Class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Member Class ---------------- #

class Member(Person):
    member_count = 0

    def __init__(self, name, age, member_id, course, department):
        super().__init__(name, age)

        # Encapsulation
        self.__member_id = member_id
        self.course = course
        self.department = department
        self.issued_books = []

        Member.member_count += 1

    def display_info(self):
        print("\n------ Member Details ------")
        print("Library      :", Person.library_name)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Member ID    :", self.__member_id)
        print("Course       :", self.course)
        print("Department   :", self.department)
        print("Issued Books :", self.issued_books if self.issued_books else "None")

    def get_member_id(self):
        return self.__member_id

    @classmethod
    def total_members(cls):
        print("Total Members :", cls.member_count)


# ---------------- Book Class ---------------- #

class Book:
    book_count = 0

    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None

        Book.book_count += 1

    def display_info(self):
        print("\n------ Book Details ------")
        print("Book ID      :", self.__book_id)
        print("Title        :", self.title)
        print("Author       :", self.author)
        print("Status       :", "Issued" if self.is_issued else "Available")

    def get_book_id(self):
        return self.__book_id

    @classmethod
    def total_books(cls):
        print("Total Books :", cls.book_count)


# ---------------- Library Class ---------------- #

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.fine_per_day = 5

    # ---------- Book Management ---------- #

    def add_book(self, book):
        self.books.append(book)
        print("\nBook Added Successfully!")

    def view_books(self):
        print("\n========== ALL BOOKS ==========")

        if not self.books:
            print("No Books Found.")
            return

        for book in self.books:
            book.display_info()

    def search_book(self, search_value):
        for book in self.books:
            if (book.get_book_id().lower() == search_value.lower()
                    or book.title.lower() == search_value.lower()):
                return book

        return None

    def delete_book(self, book_id):
        book = self.search_book(book_id)

        if book is None:
            print("\nBook Not Found.")
        elif book.is_issued:
            print("\nBook cannot be deleted because it is currently issued.")
        else:
            self.books.remove(book)
            Book.book_count -= 1
            print("\nBook Deleted Successfully!")

    # ---------- Member Management ---------- #

    def add_member(self, member):
        self.members.append(member)
        print("\nMember Registered Successfully!")

    def view_members(self):
        print("\n========== ALL MEMBERS ==========")

        if not self.members:
            print("No Members Found.")
            return

        for member in self.members:
            member.display_info()

    def search_member(self, member_id):
        for member in self.members:
            if member.get_member_id().lower() == member_id.lower():
                return member

        return None

    # ---------- Transactions ---------- #

    def issue_book(self, book_id, member_id):
        book = self.search_book(book_id)

        if book is None:
            print("\nBook Not Found.")
            return

        if book.is_issued:
            print("\nBook is Already Issued.")
            return

        member = self.search_member(member_id)

        if member is None:
            print("\nMember Not Found.")
            return

        book.is_issued = True
        book.issued_to = member.get_member_id()
        member.issued_books.append(book.title)

        print("\nBook Issued Successfully!")
        print("Book   :", book.title)
        print("Member :", member.name)

    def return_book(self, book_id, late_days=0):
        book = self.search_book(book_id)

        if book is None:
            print("\nBook Not Found.")
            return

        if not book.is_issued:
            print("\nBook is Already Available.")
            return

        member = self.search_member(book.issued_to)

        fine = self.calculate_fine(late_days)

        if member and book.title in member.issued_books:
            member.issued_books.remove(book.title)

        book.is_issued = False
        book.issued_to = None

        print("\n========== RETURN DETAILS ==========")
        print("Book       :", book.title)
        print("Late Days  :", late_days)
        print("Fine       : ₹", fine)
        print("Book returned successfully!")

    def calculate_fine(self, late_days):
        return late_days * self.fine_per_day

    def view_issued_books(self):
        print("\n========== ISSUED BOOKS ==========")

        found = False

        for book in self.books:
            if book.is_issued:
                found = True
                print("Book ID :", book.get_book_id())
                print("Title   :", book.title)
                print("Author  :", book.author)
                print("Issued To :", book.issued_to)
                print("-----------------------------")

        if not found:
            print("No Books are Currently Issued.")


# ---------------- Static Method Example ---------------- #

class LibraryPolicy:

    @staticmethod
    def library_policy():
        print("\nLibrary Policy:")
        print("1. Books must be returned on time.")
        print("2. A fine of ₹5 per late day is applicable.")
        print("3. Books should be handled carefully.")


# ---------------- Sample Objects ---------------- #

book1 = Book("V001", "Python", "Eric Matthes")
book2 = Book("V002", "Java", "Bert Bates")
book3 = Book("V003", "Web Development", "Cormen")

member1 = Member(
    "Megha", 22, "M001",
    "Computer Science", "IT"
)

member2 = Member(
    "Durga", 21, "M002",
    "Data Science", "IT"
)

library = Library()

# Add books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add members
library.add_member(member1)
library.add_member(member2)


# ---------------- Main Menu ---------------- #

def main_menu():
    while True:

        print("\n\n======================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Calculate Fine")
        print("7. Library Policy")
        print("8. View Statistics")
        print("9. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        # ---------- Book Management ---------- #
        if choice == "1":
            print("\n------ Book Management ------")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Delete Book")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                book_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")

                new_book = Book(book_id, title, author)
                library.add_book(new_book)

            elif sub_choice == "2":
                library.view_books()

            elif sub_choice == "3":
                search_value = input("Enter Book ID or Title: ")
                book = library.search_book(search_value)

                if book:
                    book.display_info()
                else:
                    print("\nBook Not Found.")

            elif sub_choice == "4":
                book_id = input("Enter Book ID: ")
                library.delete_book(book_id)

            else:
                print("\nInvalid Choice.")

        # ---------- Member Management ---------- #
        elif choice == "2":
            print("\n------ Member Management ------")
            print("1. Register Member")
            print("2. View Members")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                member_id = input("Enter Member ID: ")
                name = input("Enter Member Name: ")
                age = int(input("Enter Age: "))
                course = input("Enter Course: ")
                department = input("Enter Department: ")

                new_member = Member(
                    name, age, member_id, course, department
                )

                library.add_member(new_member)

            elif sub_choice == "2":
                library.view_members()

            else:
                print("\nInvalid Choice.")

        # ---------- Issue Book ---------- #
        elif choice == "3":
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")

            library.issue_book(book_id, member_id)

        # ---------- Return Book ---------- #
        elif choice == "4":
            book_id = input("Enter Book ID: ")

            try:
                late_days = int(
                    input("Enter number of late days (0 if on time): ")
                )
            except ValueError:
                print("\nPlease enter a valid number.")
                continue

            library.return_book(book_id, late_days)

        # ---------- Issued Books ---------- #
        elif choice == "5":
            library.view_issued_books()

        # ---------- Fine Calculation ---------- #
        elif choice == "6":
            try:
                late_days = int(input("Enter number of late days: "))

                if late_days < 0:
                    print("\nLate days cannot be negative.")
                else:
                    fine = library.calculate_fine(late_days)
                    print("\nFine Amount : ₹", fine)

            except ValueError:
                print("\nPlease enter a valid number.")

        # ---------- Library Policy ---------- #
        elif choice == "7":
            LibraryPolicy.library_policy()

        # ---------- Statistics ---------- #
        elif choice == "8":
            print("\n========== LIBRARY STATISTICS ==========")
            Book.total_books()
            Member.total_members()

        # ---------- Exit ---------- #
        elif choice == "9":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("\nInvalid Choice. Please try again.")


# ---------------- Program Execution ---------------- #

if __name__ == "__main__":
    main_menu()
