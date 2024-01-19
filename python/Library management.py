import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.state('zoomed')  # Maximize the window

        # Create SQLite database and table
        self.conn = sqlite3.connect('library.db')
        self.create_table()

        # Custom background
        self.set_custom_background()

        # Heading
        self.heading_label = tk.Label(root, text="EMERALD SCHOOL LIBRARY MANAGEMENT",
                                      font=('Arial', 25, 'bold'), fg='white', bg='#3E4095')
        self.heading_label.pack(pady=20)

        # Tabs
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill=tk.BOTH, expand=1)

        # Add Book Tab
        self.add_book_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.add_book_frame, text='Add Book')
        self.setup_add_book_ui()

        # View Books Tab
        self.view_books_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.view_books_frame, text='View Books')
        self.setup_view_books_ui()

        # Add your name label
        self.name_label = tk.Label(root, text="CREATED BY SAMARTH MOHAN - DIRECTED BY VINAY KUMAR SIR",
                                   font=('Arial', 12, 'italic'), fg='white', bg='#3E4095')
        self.name_label.pack(side=tk.BOTTOM, fill=tk.X)

    def create_table(self):
        # Create a table if it doesn't exist
        query = '''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            borrower TEXT,
            admission_number TEXT,
            class TEXT,
            section TEXT,
            date_borrowed TEXT
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def set_custom_background(self):
        # Set a custom gradient background
        bg_colors = ['#445284', '#6D77A0', '#A9BED7', '#F2F2F2']
        for i, color in enumerate(bg_colors):
            bg_label = tk.Label(self.root, bg=color)
            bg_label.place(relx=0, rely=i / len(bg_colors), relwidth=1, relheight=1 / len(bg_colors))

    def setup_add_book_ui(self):
        # Design your UI for adding books here

        # Add Book Entry Widgets
        ttk.Label(self.add_book_frame, text="Title:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.title_entry = ttk.Entry(self.add_book_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self.add_book_frame, text="Borrower's Name:").grid(row=1, column=0, padx=10,
                                                                    pady=10, sticky="w")
        self.borrower_entry = ttk.Entry(self.add_book_frame)
        self.borrower_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self.add_book_frame, text="Admission Number:").grid(row=2, column=0, padx=10,
                                                                      pady=10, sticky="w")
        self.admission_entry = ttk.Entry(self.add_book_frame)
        self.admission_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self.add_book_frame, text="Class:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.class_entry = ttk.Entry(self.add_book_frame)
        self.class_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self.add_book_frame, text="Section:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.section_entry = ttk.Entry(self.add_book_frame)
        self.section_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Add Book Button
        add_book_btn = ttk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        add_book_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def setup_view_books_ui(self):
        # Design your UI for viewing books here

        # Treeview for Book List
        self.tree = ttk.Treeview(self.view_books_frame, columns=("Title", "Borrower", "Admission Number",
                                                                "Class", "Section", "Date Borrowed"))
        self.tree.heading('#0', text='Book ID')
        self.tree.heading('Title', text='Title')
        self.tree.heading('Borrower', text='Borrower')
        self.tree.heading('Admission Number', text='Admission Number')
        self.tree.heading('Class', text='Class')
        self.tree.heading('Section', text='Section')
        self.tree.heading('Date Borrowed', text='Date Borrowed')
        self.tree['show'] = 'headings'
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.pack(fill=tk.BOTH, expand=1)

        # View Books Button
        view_books_btn = ttk.Button(self.view_books_frame, text="View Books", command=self.view_books)
        view_books_btn.pack(pady=10)

        # Delete Book Button
        delete_book_btn = ttk.Button(self.view_books_frame, text="Delete Book", command=self.delete_book)
        delete_book_btn.pack(pady=10)

        # Edit Book Button
        edit_book_btn = ttk.Button(self.view_books_frame, text="Edit Book", command=self.edit_book)
        edit_book_btn.pack(pady=10)

    def add_book(self):
        title = self.title_entry.get()
        borrower = self.borrower_entry.get()
        admission_number = self.admission_entry.get()
        class_name = self.class_entry.get()
        section = self.section_entry.get()
        date_borrowed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Validate input
        if not title or not borrower or not admission_number or not class_name or not section:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Add book to database
        query = '''
        INSERT INTO books (title, borrower, admission_number, class, section, date_borrowed)
        VALUES (?, ?, ?, ?, ?, ?);
        '''
        self.conn.execute(query, (title, borrower, admission_number, class_name, section, date_borrowed))
        self.conn.commit()

        # Clear entry fields
        self.title_entry.delete(0, tk.END)
        self.borrower_entry.delete(0, tk.END)
        self.admission_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
        self.section_entry.delete(0, tk.END)

        # Refresh book list
        self.view_books()

    def view_books(self):
        # Clear existing data in Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch book data from database
        query = '''
        SELECT * FROM books;
        '''
        result = self.conn.execute(query).fetchall()

        # Insert data into Treeview
        for row in result:
            self.tree.insert('', 'end', text=row[0], values=row[1:])

    def delete_book(self):
        # Delete selected book from the database
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Delete Book", "Please select a book to delete.")
            return

        confirm = messagebox.askyesno("Delete Book", "Are you sure you want to delete this book?")
        if confirm:
            book_id = self.tree.item(selected_item, 'text')
            query = f"DELETE FROM books WHERE id={book_id};"
            self.conn.execute(query)
            self.conn.commit()

            # Refresh book list
            self.view_books()

    def edit_book(self):
        # Edit selected book in the database
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Edit Book", "Please select a book to edit.")
            return

        book_id = self.tree.item(selected_item, 'text')
        query = f"SELECT * FROM books WHERE id={book_id};"
        result = self.conn.execute(query).fetchone()

        # Open a dialog to edit book details
        updated_data = self.edit_book_dialog(result)
        if updated_data:
            query = f'''
            UPDATE books SET
            title=?,
            borrower=?,
            admission_number=?,
            class=?,
            section=?
            WHERE id={book_id};
            '''
            self.conn.execute(query, updated_data)
            self.conn.commit()

            # Refresh book list
            self.view_books()

    def edit_book_dialog(self, book_data):
        # Open a dialog to edit book details
        updated_data = simpledialog.askstring("Edit Book", "Edit book details:",
                                              initialvalue=book_data[1:])
        if updated_data:
            updated_data = tuple(updated_data.split(", "))
            return updated_data

        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
    # done by Samarth Mohan
    # directed by Vinay Sir
