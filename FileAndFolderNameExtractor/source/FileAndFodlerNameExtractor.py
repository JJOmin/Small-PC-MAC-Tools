import os
import csv
import json
import tkinter as tk
from tkinter import filedialog, ttk

def get_folder_path():
    folder_path = filedialog.askdirectory(title="Select folder for listing")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def get_file_type():
    return file_type.get()

def get_list_type():
    return list_type.get()

def process_folder():
    directory = folder_entry.get()
    list_type_choice = get_list_type()

    if not os.path.exists(directory):
        result_label.config(text="Directory not found.", fg="red")
        return

    items = []
    if list_type_choice == 'Ordnernamen':
        items = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    elif list_type_choice == 'Dateinamen':
        items = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    elif list_type_choice == 'Ordner und Dateinamen':
        folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
        files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
        items = {'folders': folders, 'files': files}

    file_type_choice = get_file_type()
    if file_type_choice == 'csv':
        csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Save CSV File")
        if not csv_file_path:
            result_label.config(text="CSV file path not selected.", fg="red")
            return
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            if list_type_choice == 'Ordner und Dateinamen':
                csvwriter.writerow(['Type', 'Name'])
                csvwriter.writerows([['Folder', name] for name in items['folders']])
                csvwriter.writerows([['File', name] for name in items['files']])
            else:
                csvwriter.writerow([list_type_choice])
                csvwriter.writerows([[name] for name in items])

        result_label.config(text=f"{list_type_choice} have been written to {csv_file_path}.", fg="green")
    elif file_type_choice == 'json':
        json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")], title="Save JSON File")
        if not json_file_path:
            result_label.config(text="JSON file path not selected.", fg="red")
            return
        with open(json_file_path, 'w') as jsonfile:
            json.dump(items, jsonfile, indent=4)

        result_label.config(text=f"{list_type_choice} have been written to {json_file_path}.", fg="green")
    elif file_type_choice == 'xlsx':
        # Add code for saving as XLSX if required
        result_label.config(text="XLSX file saving not implemented.", fg="red")
    else:
        result_label.config(text="Invalid file type selected.", fg="red")

# Create the main window
window = tk.Tk()
window.title("List of folders into File")
window.geometry("500x350")

# Create and place widgets
folder_label = tk.Label(window, text="Select folder path:")
folder_label.pack(pady=10)

folder_entry = tk.Entry(window, width=40)
folder_entry.pack()

folder_button = tk.Button(window, text="Browse", command=get_folder_path)
folder_button.pack(pady=5)

file_type_label = tk.Label(window, text="Select File Type:")
file_type_label.pack(pady=10)

file_type = ttk.Combobox(window, values=["csv", "json", "xlsx"])
file_type.set("csv")
file_type.pack()

list_type_label = tk.Label(window, text="Select List Type:")
list_type_label.pack(pady=10)

list_type = ttk.Combobox(window, values=["Ordnernamen", "Dateinamen", "Ordner und Dateinamen"])
list_type.set("Ordnernamen")
list_type.pack()

process_button = tk.Button(window, text="Process", command=process_folder)
process_button.pack(pady=10)

result_label = tk.Label(window, text="", fg="green")
result_label.pack()

window.mainloop()
