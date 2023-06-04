#Kanishk
#Assignment 6 - 11/25/2022

import os
#importing Adult and Young from Book - A class 
from book_class import Adult, Young

# Adding book to the file
def add_book(filename, book):
    with open(filename, 'a') as f:
        f.write(", ".join([book.title, book.author, book.pub_date, book.price, book.reader, book.category]))
        f.write("\n")

# Fetching book with the author name
def view_book(filename, author):
    with open(filename, 'r') as f:
        books = f.readlines()
        book_found = False
        for curr_book in books:
            if author in curr_book.split(",")[1]:
                print(curr_book)
                book_found = True

    # Prompt if no book found
    if not book_found:
        print("No book from the given author is added.")

# Delete book functionality
def del_book(filename, author):

    book_found = False

    # Reading book
    with open(filename, 'r') as f:
        books = f.readlines()

    # Copying into other excluding target author
    with open(f"{filename}_copy", 'w') as f:
        for book in books:
            if author in book.split(',')[1]:
                book_found = True
                continue
            f.write(book)

    # Remove and rename
    os.remove(filename)
    os.rename(f"{filename}_copy", filename)

    if not book_found:
        print("No book from the given author is added.")
    else:
        print("Book Successfully Deleted")


if __name__=='__main__':

    filename = "BookShop.txt"

    # Presenting choices 
    while True:
        print("1-Add a book")
        print("2-View a book")
        print("3-View the book file")
        print("4-Delete a book")
        print("5-Exit")

        choice = input("Please enter your choice(1/2/3/4/5): ")

        # Fetching info and adding books
        if choice == '1':
            print("Please enter following information to add the book:")
            print("Note: Input is taken case sensitive")
            title = input("Book Title: ")
            author = input("Author: ")
            pub_date = input("Publication Date(Year):")
            price = input("Price: ")

            reader = input("Reader Category(Adult/Young): ")
            if reader == 'Adult':
                category = input("Sub Category(Non-fiction/Fiction): ")
                #from book class, Taking Adult and methods
                book = Adult(title=title, author=author, pub_date=pub_date, price=price, category=category)
                
                add_book(filename=filename, book=book)

            elif reader == 'Young': #From book class, Young is taken
                category = input("Sub Category(Kids/Young Adults): ")

                book = Young(title=title, author=author, pub_date=pub_date, price=price, category=category)
                
                add_book(filename=filename, book=book)
        
            print("Successfully added the book.")
            continue

        # Searching and showing the entry with the author
        elif choice == '2':
            req_author = input("Enter author's name to view:")

            view_book(filename=filename, author=req_author)

            input("Press any key to continue")
            continue
        
        # Showing the book file
        elif choice == '3':
            with open(filename, 'r') as f:
                books = f.readlines()
            i = 1
            for book in books:
                book = book.split(',')
                print("----------------------------------")
                print(f"Book No. {i}")
                print(f"Title: {book[0]}")
                print(f"Author: {book[1]}")
                print(f"Publication Date: {book[2]}")
                print(f"Price: {book[3]}")
                print(f"Readers: {book[4]}")
                print(f"Category: {book[5]}")
                i+=1
            print("----------------------------------")

        # Delete book file
        elif choice == '4':
            req_author = input("Enter author's name to delete:")
            del_book(filename=filename, author=req_author)
            continue
        
        # Quitting 
        elif choice == '5':
            break
