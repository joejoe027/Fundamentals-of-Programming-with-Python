from tkinter import filedialog

class Song():
    def __init__(self, name,file):
        self.name = name 
        self.file = file

class Playlist():
    def __init__(self):
        self.songs = []
        self.volume = 0.7

    def add_song(self,song_name):
        # Ask user to pick a file
        file_path = filedialog.askopenfilename(
            title="Select an audio file",
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )

        # If a file is chosen, load it into playlist
        if file_path:
            new_song = Song(song_name,file_path)
            self.songs.append(new_song)
            print(f"You have successfully added {new_song.name} to your playlist")
        else:
            print("No file selected.")
        
    def delete_song(self,index):
        self.songs.pop(index)

    def swap(self,index1,index2):
        temp = self.songs[index1]
        self.songs[index1] = self.songs[index2]
        self.songs[index2] = temp

    def reOrder(self,picked_song_index,new_song_index):
        picked_song = self.songs[picked_song_index]
        self.songs.pop(picked_song_index)
        self.songs.insert(new_song_index,picked_song)

    def nextSong(self,index):
        if index >= len(self.songs):
            return (self.songs[0],0)
        elif index < 0:
            return (self.songs[len(self.songs) - 1],len(self.songs) - 1)
        else:
            return (self.songs[index],index)
