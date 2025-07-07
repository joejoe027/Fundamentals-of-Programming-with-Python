from classes import Playlist
from pygame import mixer 

def play(playlist):
    mixer.init()

    if not playlist.songs:
            print("You currently have no songs!")
            return
    else:
        print("Here is your playlist!")
        for i in range(len(playlist.songs)):
            print(f"{i + 1}. {playlist.songs[i].name}")
    
    index = 0
    playing_song = False
    toggle = 1
    
    while True:
        if not playing_song:
            current_song, index = playlist.nextSong(index)
            print(f"Currently playing {current_song.name}")

            # Loading the song
            mixer.music.load(current_song.file)

            # Setting the volume
            mixer.music.set_volume(playlist.volume)

            # Start playing the song
            mixer.music.play()
            
            playing_song = True

            
        if toggle == 1:
            print("1. Pause")
        else:
            print("1. Unpause")

        print("2. Increase Volume")
        print("3. Decrease Volume")
        print("4. Next Song")
        print("5. Previous Song")
        print("6. Exit Playlist")
        print(f"Current Volume: {round(playlist.volume,1)}")
        command = int(input("Please enter a command: "))

        if command == 1:
            # Pausing/unpausing the music
            if toggle == 1:
                mixer.music.pause()  
                toggle = 0 
            else:  
                mixer.music.unpause()
                toggle = 1
        elif command == 2:
            if round(playlist.volume,1) < 1:
                playlist.volume += 0.1
            mixer.music.set_volume(playlist.volume)
        elif command == 3:
            if round(playlist.volume,1) > 0:
                playlist.volume -= 0.1
            mixer.music.set_volume(playlist.volume)
        elif command == 4:
            mixer.music.stop()
            index += 1
            playing_song = False
        elif command == 5:
            mixer.music.stop()
            index -= 1
            playing_song = False
        elif command == 6:
            mixer.music.stop()
            return
        
def edit(playlist):
    while True:

        if not playlist.songs:
            print("You currently have no songs!")
        else:
            for i in range(len(playlist.songs)):
                print(f"{i + 1}. {playlist.songs[i].name}")

        print("-----------------------")
        print("1. Add a song")
        print("2. Delete a song")
        print("3. Swap Orders")
        print("4. Re-order")
        print("5. Exit")
        print("-----------------------")
        command = int(input("Enter a command: "))

        if command == 1:
            song_name = input("Enter name of the song: ")
            playlist.add_song(song_name)
        elif command == 2:
            delete_song_index = int(input("Pick the song you want to delete: ")) - 1
            playlist.delete_song(delete_song_index)
        elif command == 3:
            song1_index = int(input("Pick first song: ")) - 1
            song2_index = int(input("Pick second song: ")) - 1

            playlist.swap(song1_index, song2_index)
        elif command == 4:
            picked_song_index = int(input("Enter the song you want to change its order: ")) - 1
            new_song_index = int(input("Enter the new index for this song: ")) - 1

            playlist.reOrder(picked_song_index,new_song_index)
        elif command == 5:
            break
        else:
            print("Invalid command")
def main():
    print("Welcome to music player!")
    playlist = Playlist()
    while True:
        print("-----------------------")
        print("1. Play your playlist")
        print("2. Edit your playlist")
        print("3. Exit")
        print("-----------------------")
        command = int(input("Enter a command: "))

        if command == 1:
            play(playlist)
        elif command == 2:
            edit(playlist)
        elif command == 3:
            return
        else:
            print("Invalid command")

main()
