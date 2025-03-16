import json
# Load data from JSON file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to JSON file
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Display the library
def view_library(library):
    if not library:
        print("Your Library is empty. Please add books!")
        return
    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")

# Add a new book
def add_book(library):
    print("\nAdd a New Book")
    book = {
        "title": input("Enter Title: "),
        "author": input("Enter Author: "),
        "year": int(input("Enter Year: ")),
        "genre": input("Enter Genre: "),
        "read_status": input("Mark as Read? (y/n): ").lower() == "y"
    }
    library.append(book)
    save_library(library)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    if not library:
        print("No books in the library to remove!")
        return
    print("\nRemove a Book")
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']}")
    try:
        choice = int(input("Enter the number of the book to remove: "))
        if 1 <= choice <= len(library):
            removed_book = library.pop(choice - 1)
            save_library(library)
            print(f"Book '{removed_book['title']}' removed successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

# Search for a book
def search_book(library):
    search_term = input("\nEnter Title or Author to search: ").lower()
    results = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]
    if not results:
        print("No books found!")
        return
    print("\nSearch Results:")
    for idx, book in enumerate(results, start=1):
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read_status'] else 'No'}")

# Main CLI function
def main():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. View Library")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Save & Exit")
        choice = input("Select an option (1-5): ")

        actions = {
            "1": view_library,
            "2": add_book,
            "3": remove_book,
            "4": search_book,
            "5": lambda: (save_library(library), print("Library saved successfully!  Goodbye!..."), exit())
        }

        action = actions.get(choice, lambda: print("Invalid choice! Please select a valid option."))
        action(library) if choice != "5" else action()

if __name__ == "__main__":
    main()
