from tkinter import filedialog

def find_file_path(song_name):

    file_path = filedialog.askopenfilename(
        title="Select an MP3 or WAV file",
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )

    if file_path:
        print(f"'{song_name}' added to your playlist!")
    else:
        print("No file selected.")
    
    return file_path

file_path = find_file_path("Song 1")
print(file_path)
