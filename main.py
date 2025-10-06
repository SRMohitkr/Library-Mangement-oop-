                            # Library Management System #
# This program allows users to add and borrow books from a library.

class Library:
    def __init__(self,book,no_of_book):
        self.book = book
        self.no_of_book = no_of_book
# add method
    def add(self,book,no_of_book):
        self.book = book
        self.no_of_book= no_of_book
        with open("library.txt","a") as f:
            f.write(f"Book Name: {self.book}\n")
            f.write(f"Number of Books: {self.no_of_book}\n")

        print(f"✅ Added {self.no_of_book} copies of '{self.book}'.")
# borrow method
    def borrow(self,book,no_of_book):
        self.book = book
        self.no_of_book= no_of_book

        with open("library.txt","r") as f:
            lines = f.readlines()
        
        new_lines = []
        i = 0
        a=0
        borrowed = False

        while i < len(lines):
            a+=1
            line = lines[i].strip()
            if line == f"Book Name: {self.book}":
                available_copies = int(lines[i+1].strip().split(": ")[1])
                if available_copies >= self.no_of_book:
                    new_count = available_copies - self.no_of_book
                    new_lines.append(f"Book Name: {self.book}\n")
                    new_lines.append(f"Number of Books: {new_count}\n")
                    print(f"✅ Borrowed {self.no_of_book} copies of '{self.book}'.")
                    borrowed = True
                else:
                    print(f"❌ Not enough copies of '{self.book}' available.")
                    new_lines.append(lines[i])
                    new_lines.append(lines[i+1])
                i += 2
            else:
                new_lines.append(lines[i])
                i += 1

        with open("library.txt", "w") as f:
            f.writelines(new_lines)

        if not borrowed:
            print(f"❌ Book '{self.book}' not available in library.")
# count method
    def count(self):
            with open("library.txt", "r") as f:
                print("\n📚 Current Library Collection:\n" + f.read())
#total method
    def total(self):
        try:
            with open("library.txt", "r") as f:
                lines = f.readlines()

            total_books = 0
            for line in lines:
                if line.startswith("Number of Books:"):
                    total_books += int(line.split(": ")[1])

            print(f"\n📚 Total number of books in library: {total_books}\n")

        except FileNotFoundError:
            print("Library is empty.")


libriarian = Library("","")
while True:
    ask = input("\nDo you want to(add(a)/borrow(b)/count(c)/total(t)/exit(e)): ").strip().lower()

    if ask == 'add'or ask =="a":
        book_name = input("Enter the book name to add: ").strip().lower()
        num_copies = int(input("Enter the number of copies to add: "))
        libriarian.add(book_name, num_copies)
    elif ask == "borrow"or ask =="b":
        book_name = input("Enter the book name to borrow: ").strip().lower()
        num_copies = int(input("Enter the number of copies to borrow: "))
        libriarian.borrow(book_name, num_copies)
    elif ask == 'exit' or ask =="e":
        print("Exiting the program.")
        break
    elif ask == 'count'or ask =="c":
        libriarian.count()

    elif ask == 'total'or ask =="t":
        libriarian.total()
    else:
        print("Invalid choice. Please try again.")
