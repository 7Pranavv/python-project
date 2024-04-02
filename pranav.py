import os

# Function to load data from file
def load_data(file_path):
    books = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                books.append(line.strip().split(','))
    return books

# Function to save data to file
def save_data(books, file_path):
    with open(file_path, 'w') as file:
        for book in books:
            file.write(','.join(book) + '\n')

# Function to display menu
def display_menu():
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Exit")
    print("=====================================")

# Function to add a book
def add_book(books):
    title = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    books.append((title, author))
    print("Book added successfully!")

# Function to remove a book
def remove_book(books):
    title = input("Enter title of the book to remove: ")
    author = input("Enter author of the book to remove: ")
    if (title, author) in books:
        books.remove((title, author))
        print("Book removed successfully!")
    else:
        print("Book not found!")

# Function to display all books
def display_books(books):
    if books:
        print("===== Books Available =====")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. {book[0]} by {book[1]}")
        print("==========================")
    else:
        print("No books available.")

# Main function
def main():
    file_path = "library_data.txt"
    books = load_data(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            save_data(books, file_path)
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
