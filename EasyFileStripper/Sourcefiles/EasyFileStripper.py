import os
import shutil
import tkinter as tk
from tkinter import filedialog

def extract_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.copy2(source_path, destination_path)
            print(f"Copying {file} to {destination_folder}")

def choose_source_folder():
    folder_path = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder_path)

def choose_destination_folder():
    folder_path = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, folder_path)

def extract_button_clicked():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()
    extract_files(source_folder, destination_folder)
    print("File extraction complete!")

app = tk.Tk()
app.title("File Extractor")
app.geometry("300x200")

source_label = tk.Label(app, text="Source Folder:")
source_label.pack()

source_entry = tk.Entry(app)
source_entry.pack()

source_button = tk.Button(app, text="Choose Source", command=choose_source_folder)
source_button.pack()

destination_label = tk.Label(app, text="Destination Folder:")
destination_label.pack()

destination_entry = tk.Entry(app)
destination_entry.pack()

destination_button = tk.Button(app, text="Choose Destination", command=choose_destination_folder)
destination_button.pack()

extract_button = tk.Button(app, text="Extract Files", command=extract_button_clicked)
extract_button.pack()

app.mainloop()