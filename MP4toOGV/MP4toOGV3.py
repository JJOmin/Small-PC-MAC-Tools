import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from moviepy.editor import *
from threading import Thread
import time  # Import the time module

# Function to display ongoing conversion with dots
def display_ongoing_conversion():
    dots = 0
    while converting:
        dots = (dots + 1) % 4
        result_label.config(text="Converting ongoing" + "." * dots)
        time.sleep(1)

# Function to stop displaying ongoing conversion
def stop_display_ongoing_conversion():
    global converting
    converting = False
    result_label.config(text="Conversion completed!")


# Funktion zum Konvertieren von Videos
def convert_videos():
    def conversion_thread():
        global converting
        converting = True
        input_option = input_option_var.get()
        input_path = input_entry.get()
        output_folder = output_folder_entry.get()
        resize_resolution = resize_resolution_entry.get()
        codec_option = codec_var.get()
        bitrate_option = bitrate_entry.get()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if input_option == "Folder":
            video_files = [filename for filename in os.listdir(input_path) if filename.endswith(".mp4")]
            total_videos = len(video_files)

            for i, filename in enumerate(video_files):
                input_file_path = os.path.join(input_path, filename)
                output_filename = os.path.splitext(filename)[0] + ".ogv"  # Ensure .ogv extension
                output_path = os.path.join(output_folder, output_filename)

                video_clip = VideoFileClip(input_file_path)

                # Überprüfe, ob die Auflösung geändert werden soll
                if resize_resolution:
                    width, height = map(int, resize_resolution.split('x'))
                    video_clip = video_clip.resize((width, height))

                # Specify the video codec as 'libtheora' and audio codec as 'libvorbis'
                video_clip.write_videofile(output_path, codec='libtheora', audio_codec='libvorbis')

        elif input_option == "File":
            if input_path.endswith(".mp4"):
                output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".ogv"
                output_path = os.path.join(output_folder, output_filename)

                video_clip = VideoFileClip(input_path)

                # Überprüfe, ob die Auflösung geändert werden soll
                if resize_resolution:
                    width, height = map(int, resize_resolution.split('x'))
                    video_clip = video_clip.resize((width, height))

                video_clip.write_videofile(output_path, codec=codec_option, bitrate=bitrate_option)
        
        result_label.config(text="Conversion completed!")
        stop_display_ongoing_conversion()

        if exit_on_done_var.get():
            root.quit()

    convert_thread = Thread(target=conversion_thread)
    convert_thread.start()
    display_ongoing_conversion()  # Start displaying ongoing conversion

# Funktion zum Überprüfen, ob MoviePy installiert ist
def check_moviepy_installed():
    try:
        import moviepy
        messagebox.showinfo("Moviepy Installed", "Moviepy is installed!")
    except ImportError:
        messagebox.showerror("Moviepy Not Installed", "Moviepy is not installed!")

# Funktion zum Auswählen des Quellordners oder der Quelldatei
def choose_input():
    input_option = input_option_var.get()

    if input_option == "Folder":
        input_folder = filedialog.askdirectory()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_folder)
    elif input_option == "File":
        input_file = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)

# Funktion zum Auswählen des Ausgabeordners
def choose_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)

# GUI-Erstellung
root = tk.Tk()
root.title("Video Converter")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_option_var = tk.StringVar(value="Folder")
codec_var = tk.StringVar(value="libtheora")
bitrate_var = tk.StringVar(value="50000k")  # Vordefinierte Bitrate

input_option_label = ttk.Label(main_frame, text="Select input type:")
input_option_label.grid(column=0, row=0, columnspan=2, pady=5)

input_option_menu = ttk.OptionMenu(main_frame, input_option_var, "Folder", "Folder", "File")
input_option_menu.grid(column=2, row=0, columnspan=2, pady=5)

input_label = ttk.Label(main_frame, text="Input (Folder or File):")
input_label.grid(column=0, row=1, columnspan=2, pady=5)

input_entry = ttk.Entry(main_frame)
input_entry.grid(column=2, row=1, columnspan=2, pady=5)

input_button = ttk.Button(main_frame, text="Select", command=choose_input)
input_button.grid(column=4, row=1, pady=5)

output_label = ttk.Label(main_frame, text="Output folder for OGV files:")
output_label.grid(column=0, row=2, columnspan=2, pady=5)

output_folder_entry = ttk.Entry(main_frame)
output_folder_entry.grid(column=2, row=2, columnspan=2, pady=5)

output_button = ttk.Button(main_frame, text="Select", command=choose_output_folder)
output_button.grid(column=4, row=2, pady=5)

resize_resolution_label = ttk.Label(main_frame, text="Resize Resolution (Optional):")
resize_resolution_label.grid(column=0, row=3, columnspan=2, pady=5)

resize_resolution_entry = ttk.Entry(main_frame)
resize_resolution_entry.grid(column=2, row=3, columnspan=2, pady=5)

codec_label = ttk.Label(main_frame, text="Codec:")
codec_label.grid(column=0, row=4, columnspan=2, pady=5)

codec_menu = ttk.OptionMenu(main_frame, codec_var, "libtheora", "libtheora", "libx264")
codec_menu.grid(column=2, row=4, columnspan=2, pady=5)

bitrate_label = ttk.Label(main_frame, text="Bitrate (Optional):")
bitrate_label.grid(column=0, row=5, columnspan=2, pady=5)

bitrate_entry = ttk.Entry(main_frame, textvariable=bitrate_var)  # Verknüpfe das Eingabefeld mit der Bitrate-Variable
bitrate_entry.grid(column=2, row=5, columnspan=2, pady=5)

convert_button = ttk.Button(main_frame, text="Convert Videos", command=convert_videos)
convert_button.grid(column=0, row=6, columnspan=5, pady=10)

check_moviepy_button = ttk.Button(main_frame, text="Check Moviepy", command=check_moviepy_installed)
check_moviepy_button.grid(column=0, row=7, columnspan=5, pady=5)


result_label = ttk.Label(main_frame, text="")
result_label.grid(column=0, row=9, columnspan=5, pady=10)

root.mainloop()