import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # Import from Pillow

# Decorator for logging method calls and adding basic error handling
def log_method(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Method {func.__name__} called with arguments: {args[1:]}")
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
    return wrapper

# Base class for handling book data (encapsulation)
class BookDatabase:
    def __init__(self):
        # Dictionary to hold book data (title: (author, publication year, ISBN, available copies))
        self.books = {
            "Automate the Boring Stuff with Python": ("Al Sweigart", 2019, "978-1593279929", 5),
            "The C Programming Language": ("Brian W. Kernighan, Dennis M. Ritchie", 1988, "978-0131103627", 3),
            "Python Crash Course": ("Eric Matthes", 2015, "978-1593279288", 7),
            "Effective Modern C++": ("Scott Meyers", 2014, "978-1491903991", 4),
            # Add more books here...
        }

    @log_method
    def search_by_title(self, title):
        title = title.lower()
        return [f"{book} - {self.books[book][0]} (Published: {self.books[book][1]})"
                for book in self.books if title in book.lower()]

    @log_method
    def add_book(self, title, author, year, isbn, copies):
        # Add book to the database
        self.books[title] = (author, year, isbn, copies)

# GUI class using multiple inheritance to inherit both Tkinter functionality and BookDatabase logic
class LibraryManagementSystem(tk.Tk, BookDatabase):
    def __init__(self):
        tk.Tk.__init__(self)  # Initialize Tkinter root window
        BookDatabase.__init__(self)  # Initialize Book Database
        self.title("Welcome to Booklover Library")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")  # Light grey background

        # Set up the UI
        self.create_widgets()

    def create_widgets(self):
        try:
            # Load and set the background image using Pillow
            image = Image.open("Book.png")                    # Assuming 'book.png' is in the same directory
            self.background_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage
            self.background_label = tk.Label(self, image=self.background_image)
            self.background_label.place(relwidth=1, relheight=1)  # Cover the whole window

            # Add welcome label
            self.welcome_label = tk.Label(self, text="Welcome to Book Lover Library", bg="#f0f0f0", font=("Helvetica", 16))
            self.welcome_label.pack(pady=20)

            # Frame for buttons
            self.button_frame = tk.Frame(self, bg="#f0f0f0")
            self.button_frame.pack(side=tk.BOTTOM, pady=20)  # Pack at the bottom with padding

            # Search Book button
            self.search_button = tk.Button(self.button_frame, text="Search a Book", command=self.open_search_window)
            self.search_button.pack(side=tk.LEFT, padx=5)  # Pack to the left with padding

            # Add Book button
            self.add_book_button = tk.Button(self.button_frame, text="Add Book", command=self.add_new_book)
            self.add_book_button.pack(side=tk.LEFT, padx=5)  # Pack to the left with padding

        except Exception as e:
            print(f"Error creating widgets: {e}")
            messagebox.showerror("Error", f"An error occurred while creating widgets: {e}")

    def open_search_window(self):
        # Create a new window for searching books
        search_window = tk.Toplevel(self)  # Create a new top-level window
        search_window.title("Search for a Book")
        search_window.geometry("400x200")
        search_window.configure(bg="#f0f0f0")

        search_label = tk.Label(search_window, text="Enter book title:", bg="#f0f0f0", font=("Helvetica", 12))
        search_label.pack(pady=10)

        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)

        search_button = tk.Button(search_window, text="Search", command=lambda: self.search_book(search_entry.get(), search_window))
        search_button.pack(pady=5)

        clear_button = tk.Button(search_window, text="Clear", command=lambda: self.clear_search(search_entry))
        clear_button.pack(pady=5)

    @log_method  # Decorator to log search actions
    def search_book(self, search_text, search_window):
        try:
            results = self.search_by_title(search_text)  # Use the encapsulated search method

            if results:
                result_text = "\n".join(results)  # Join all results into a single string
                messagebox.showinfo("Search Results", result_text)  # Show results in a message box
            else:
                messagebox.showinfo("No Matches Found", f"No books found matching '{search_text}'.")

            search_window.destroy()  # Close the search window after the search

        except Exception as e:
            print(f"Error in search_book: {e}")
            messagebox.showerror("Error", f"An error occurred while searching: {e}")

    @log_method  # Clear search action
    def clear_search(self, entry):
        try:
            entry.delete(0, tk.END)  # Clear the search box
        except Exception as e:
            print(f"Error in clear_search: {e}")
            messagebox.showerror("Error", f"An error occurred while clearing the search: {e}")

    @log_method  # Method to add a new book
    def add_new_book(self):
        try:
            # Dialog to get new book information
            title = simpledialog.askstring("Book Title", "Enter the book title:")
            author = simpledialog.askstring("Author", "Enter the author's name:")
            year = simpledialog.askinteger("Publication Year", "Enter the publication year:")
            isbn = simpledialog.askstring("ISBN", "Enter the ISBN number:")
            copies = simpledialog.askinteger("Copies Available", "Enter the number of available copies:")

            if title and author and year and isbn and copies:
                self.add_book(title, author, year, isbn, copies)
                messagebox.showinfo("Success", f"Book '{title}' added successfully!")
            else:
                messagebox.showwarning("Input Error", "All fields must be filled out to add a new book.")

        except Exception as e:
            print(f"Error in add_new_book: {e}")
            messagebox.showerror("Error", f"An error occurred while adding a new book: {e}")

# Subclass to demonstrate method overriding and polymorphism
class AdvancedLibrarySystem(LibraryManagementSystem):
    def __init__(self):
        super().__init__()

    # Override search functionality to add additional search methods
    @log_method
    def search_by_title(self, title):
        title = title.lower()
        return [f"{book} - {self.books[book][0]} (Published: {self.books[book][1]})"
                for book in self.books if title in book.lower()]

if __name__ == "__main__":
    app = AdvancedLibrarySystem()  # Using the subclass to demonstrate method overriding
    app.mainloop()
