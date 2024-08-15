import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import threading

root = tk.Tk()
root.title("Music Player")

def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            audio = AudioSegment.from_file(file_path)
            threading.Thread(target=play, args=(audio,)).start()
        except Exception as e:
            print(f"Error: {e}")

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()
