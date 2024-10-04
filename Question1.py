import tkinter as tk
from tkinter import PhotoImage, Label, messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Booklover Library")
        self.root.geometry("600x400")

        # Set background color
        self.root.configure(bg="#f0f0f0")  # Light grey background

        # Load and set the background image
        self.background_image = PhotoImage(file=r"C:\Users\Musra\OneDrive\Pictures\book.png")  # Replace with your image path
        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)  # Cover the whole window

        # Add welcome label
        self.welcome_label = Label(root, text="Welcome to Book Lover Library", bg="#f0f0f0", font=("Helvetica", 16))
        self.welcome_label.pack(pady=20)

        # Frame for search options
        self.search_frame = tk.Frame(root, bg="#f0f0f0")
        self.search_frame.pack(side=tk.BOTTOM, pady=20)  # Pack at the bottom with padding

        self.search_label = Label(self.search_frame, text="Search for a Book:", bg="#f0f0f0", font=("Helvetica", 12))
        self.search_label.pack(side=tk.LEFT)  # Pack to the left

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)  # Pack to the left with padding

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_book)
        self.search_button.pack(side=tk.LEFT)  # Pack to the left

        # Dictionary to hold book data (title: (author, publication year, ISBN, available copies))
        self.books = {
            "Automate the Boring Stuff with Python": ("Al Sweigart", 2019, "978-1593279929", 5),
            "The C Programming Language": ("Brian W. Kernighan, Dennis M. Ritchie", 1988, "978-0131103627", 3),
            "C++ Primer": ("Stanley B. Lippman, Josée Lajoie, Barbara E. Moo", 2012, "978-0321992789", 4),
            "Laravel: Up and Running": ("Matt Stauffer", 2019, "978-1491933652", 6),
            "Pro ASP.NET Core MVC 2": ("Adam Freeman", 2017, "978-1484230153", 2),
            "Python Crash Course": ("Eric Matthes", 2015, "978-1593279288", 7),
            "C Programming: A Modern Approach": ("K. N. King", 2008, "978-0393979503", 3),
            "Effective Modern C++": ("Scott Meyers", 2014, "978-1491903991", 4),
            "Laravel 8: The Complete Guide to Building Applications with Laravel": ("Andrew Coyle", 2021, "978-1838821045", 5),
            "C# in Depth": ("Jon Skeet", 2019, "978-1617294532", 3),
        }

        # Label to display search results
        self.result_label = Label(root, bg="#f0f0f0", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def search_book(self):
        # Functionality to search for a book
        search_text = self.search_entry.get().lower()  # Get the search text in lowercase
        matches = []

        # Iterate through the book titles and check for matches
        for title, (author, year, isbn, available) in self.books.items():
            if search_text in title.lower():  # Check if search text is in title
                matches.append(f"{title} (Author: {author})")  # Format to show title and author

        # Update the result label based on matches
        if matches:
            result_text = "\n".join(f"Book {i+1}: {match}" for i, match in enumerate(matches))  # Number the matches
            self.result_label.config(text=result_text)  # Show all matching results
        else:
            messagebox.showinfo("No Matches Found", f"No books found matching '{search_text}'.")
            self.result_label.config(text="")  # Clear previous results if no matches

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
