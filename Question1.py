import tkinter as tk
from tkinter import messagebox
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
            image = Image.open("book.png")  # Assuming 'book.png' is in the same directory
            self.background_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage
            self.background_label = tk.Label(self, image=self.background_image)
            self.background_label.place(relwidth=1, relheight=1)  # Cover the whole window

            # Add welcome label
            self.welcome_label = tk.Label(self, text="Welcome to Book Lover Library", bg="#f0f0f0", font=("Helvetica", 16))
            self.welcome_label.pack(pady=20)

            # Frame for search options
            self.search_frame = tk.Frame(self, bg="#f0f0f0")
            self.search_frame.pack(side=tk.BOTTOM, pady=20)  # Pack at the bottom with padding

            self.search_label = tk.Label(self.search_frame, text="Search for a Book:", bg="#f0f0f0", font=("Helvetica", 12))
            self.search_label.pack(side=tk.LEFT)  # Pack to the left

            self.search_entry = tk.Entry(self.search_frame)
            self.search_entry.pack(side=tk.LEFT, padx=5)  # Pack to the left with padding

            # Bind the Enter key to trigger search
            self.search_entry.bind('<Return>', lambda event: self.search_book())

            self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_book)
            self.search_button.pack(side=tk.LEFT)  # Pack to the left

            self.clear_button = tk.Button(self.search_frame, text="Clear", command=self.clear_search)  # Clear button
            self.clear_button.pack(side=tk.LEFT, padx=5)  # Pack to the left with padding

            # Label to display search results
            self.result_label = tk.Label(self, bg="#f0f0f0", font=("Helvetica", 12))
            self.result_label.pack(pady=20)

        except Exception as e:
            print(f"Error creating widgets: {e}")
            messagebox.showerror("Error", f"An error occurred while creating widgets: {e}")

    @log_method  # Decorator to log search actions
    def search_book(self):
        try:
            search_text = self.search_entry.get().lower()  # Get the search text
            results = self.search_by_title(search_text)  # Use the encapsulated search method

            if results:
                result_text = "\n".join(results)  # Join all results into a single string
                self.result_label.config(text=result_text)
            else:
                messagebox.showinfo("No Matches Found", f"No books found matching '{search_text}'.")
                self.result_label.config(text="")  # Clear previous results

            self.search_entry.delete(0, tk.END)  # Clear the search box after displaying the results

        except Exception as e:
            print(f"Error in search_book: {e}")
            messagebox.showerror("Error", f"An error occurred while searching: {e}")

    @log_method  # Clear search action
    def clear_search(self):
        try:
            self.search_entry.delete(0, tk.END)  # Clear the search box
            self.result_label.config(text="")  # Clear the results label
        except Exception as e:
            print(f"Error in clear_search: {e}")
            messagebox.showerror("Error", f"An error occurred while clearing the search: {e}")

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
