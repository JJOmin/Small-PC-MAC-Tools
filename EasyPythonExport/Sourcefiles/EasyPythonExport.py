import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_script():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    script_entry.delete(0, tk.END)
    script_entry.insert(0, file_path)

def select_output_dir():
    dir_path = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, dir_path)

def run_pyinstaller():
    script_path = script_entry.get()
    output_dir = output_dir_entry.get()

    if script_path and output_dir:
        quoted_script_path = f'"{script_path}"'
        quoted_output_dir = f'"{output_dir}"'

        # Set the working directory to the output directory
        os.chdir(output_dir)
        
        command = f"pyinstaller --onefile --distpath {quoted_output_dir} {quoted_script_path}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.stdout)
        output_text.insert(tk.END, result.stderr)
        output_text.config(state=tk.DISABLED)

        if close_checkbox_var.get():
            root.destroy()

# Create the main window
root = tk.Tk()
root.title("PyInstaller Runner")

# Create and place widgets
script_label = tk.Label(root, text="Select Python Script:")
script_label.pack()

script_entry = tk.Entry(root, width=50)
script_entry.pack()

select_button = tk.Button(root, text="Select Script", command=select_script)
select_button.pack()

output_dir_label = tk.Label(root, text="Select Output Directory:")
output_dir_label.pack()

output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.pack()

select_output_button = tk.Button(root, text="Select Output Directory", command=select_output_dir)
select_output_button.pack()

close_checkbox_var = tk.IntVar()
close_checkbox = tk.Checkbutton(root, text="Close when Done", variable=close_checkbox_var)
close_checkbox.pack()

run_button = tk.Button(root, text="Run PyInstaller", command=run_pyinstaller)
run_button.pack()

output_text = tk.Text(root, height=10, width=60)
output_text.pack()

output_text.config(state=tk.DISABLED)

# Start the GUI event loop
root.mainloop()