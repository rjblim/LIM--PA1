def display_playlist():
    songs = ["ILYSB", "Falling For You", "All I Need To Hear"]

    print("\n===== MY PLAYLIST =====")
    for number, song in enumerate(songs, start=1):
        print(f"{number}. {song}")