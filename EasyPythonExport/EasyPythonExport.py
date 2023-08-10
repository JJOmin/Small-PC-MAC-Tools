import tkinter as tk
from tkinter import filedialog
import subprocess

def select_script():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    script_entry.delete(0, tk.END)
    script_entry.insert(0, file_path)

def export_exe():
    script_path = script_entry.get()
    
    try:
        subprocess.run(["pyinstaller", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        warning_label.config(text="PyInstaller not found!")
        return
    
    if script_path:
        cmd = f"pyinstaller --onefile {script_path}"
        subprocess.run(cmd, shell=True)
        warning_label.config(text="EXE exported successfully!")

# Create the main window
root = tk.Tk()
root.title("PyInstaller Exporter")
root.geometry("400x110")


# Create and place widgets
script_label = tk.Label(root, text="Select Python Script:")
script_label.pack()

script_entry = tk.Entry(root, width=50)
script_entry.pack()

select_button = tk.Button(root, text="Select Script", command=select_script)
select_button.pack()

export_button = tk.Button(root, text="Export EXE", command=export_exe)
export_button.pack()

warning_label = tk.Label(root, text="")
warning_label.pack()

# Start the GUI event loop
root.mainloop()
