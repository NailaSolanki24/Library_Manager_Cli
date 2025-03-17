import json
import os

data_file = 'library.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []  # Fix: Empty list return karna zaroori hai

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully!')

def remove_book(library):
    title = input('Enter the title of the book to remove from the library: ')
    initial_length = len(library)
    updated_library = [book for book in library if book['title'] != title]

    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f'Book "{title}" removed successfully!')
        return updated_library  # Fix: Updated list return karni zaroori hai
    else:
        print(f'Book "{title}" not found in the library!')
        return library

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    search_term = input(f'Enter the {search_by}: ').lower()

    if search_by not in ["title", "author"]:
        print("Invalid search type. Please search by 'title' or 'author'.")
        return

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = 'read' if book['read'] else 'not read'
            print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = 'read' if book['read'] else 'not read'
            print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, {status}")
    else:
        print('No books in the library.')  # Fix: Incorrect indentation

def display_statistics(library):
    total_books = len(library)
    total_read = len([book for book in library if book['read']])
    percentage_read = (total_read / total_books) * 100 if total_books > 0 else 0
    print(f'Total books: {total_books}')
    print(f'Percentage read: {percentage_read:.2f}%')  # Fix: Spelling mistake

def main():
    library = load_data()  # Fix: load_data() ab hamesha list return karega

    while True:
        print('\nWelcome to the Library Manager!')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search the library')
        print('4. Display all books')
        print('5. Display statistics')
        print('6. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)  # Fix: Updated library return karni zaroori hai
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print('Goodbye! Have a nice day!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
