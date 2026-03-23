import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
from organizer import FileOrganizer, categorize_file

selected_folder = ""

def select_folder():
    global selected_folder
    folder = filedialog.askdirectory()
    if folder:
        selected_folder = folder
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder)
        load_files()

def load_files():
    for row in tree.get_children():
        tree.delete(row)

    if not selected_folder:
        return

    for file in os.listdir(selected_folder):
        full_path = os.path.join(selected_folder, file)
        if os.path.isfile(full_path):
            category = categorize_file(full_path)
            tree.insert("", "end", values=(file, category))

def run_organizer():
    if not selected_folder:
        messagebox.showerror("Error", "Select folder first")
        return

    organizer = FileOrganizer(selected_folder)
    organizer.organize_files()
    organizer.handle_duplicates()
    organizer.suggest_cleanup()

    messagebox.showinfo("Done", "Files organized 🚀")
    load_files()

# UI
root = tk.Tk()
root.title("Intelligent File Organizer")
root.geometry("700x400")

# Path
entry_path = tk.Entry(root, width=60)
entry_path.pack(pady=10)

btn_browse = tk.Button(root, text="Browse Folder", command=select_folder)
btn_browse.pack()

# Table (Explorer view)
columns = ("File Name", "Category")
tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("File Name", text="File Name")
tree.heading("Category", text="Category")

tree.pack(fill="both", expand=True, pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

btn_refresh = tk.Button(btn_frame, text="Refresh", command=load_files)
btn_refresh.grid(row=0, column=0, padx=10)

btn_run = tk.Button(btn_frame, text="Organize Files", command=run_organizer)
btn_run.grid(row=0, column=1, padx=10)

root.mainloop()