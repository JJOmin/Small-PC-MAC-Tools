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

def get_folder_names():
    directory = folder_entry.get()

    if not os.path.exists(directory):
        result_label.config(text="Directory not found.", fg="red")
        return

    folder_names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    file_type_choice = get_file_type()
    if file_type_choice == 'csv':
        csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Save CSV File")
        if not csv_file_path:
            result_label.config(text="CSV file path not selected.", fg="red")
            return
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Folder Names'])
            csvwriter.writerows([[name] for name in folder_names])

        result_label.config(text=f"Folders have been written to {csv_file_path}.", fg="green")
    elif file_type_choice == 'json':
        json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")], title="Save JSON File")
        if not json_file_path:
            result_label.config(text="JSON file path not selected.", fg="red")
            return
        with open(json_file_path, 'w') as jsonfile:
            json.dump(folder_names, jsonfile, indent=4)

        result_label.config(text=f"Folders have been written to {json_file_path}.", fg="green")
    elif file_type_choice == 'xlsx':
        # Add code for saving as XLSX if required
        result_label.config(text="XLSX file saving not implemented.", fg="red")
    else:
        result_label.config(text="Invalid file type selected.", fg="red")

# Create the main window
window = tk.Tk()
window.title("List of folders into File")
window.geometry("500x250")

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

process_button = tk.Button(window, text="Process Folders", command=get_folder_names)
process_button.pack(pady=10)

result_label = tk.Label(window, text="", fg="green")
result_label.pack()

window.mainloop()
