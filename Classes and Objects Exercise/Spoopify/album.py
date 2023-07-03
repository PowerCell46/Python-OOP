class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = []
        self.song_names = []
        for el in songs:
            self.songs.append(el)
            self.song_names.append(el.name)

    def add_song(self, song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        self.song_names.append(song.name)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if song_name not in self.song_names:
            return f'Song is not in the album.'
        if self.published:
            return f'Cannot remove songs. Album is published.'
        search_index = self.song_names.index(song_name)
        self.song_names.pop(search_index)
        removed_song = self.songs.pop(search_index)
        return f'Removed song {removed_song.name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        return_list = []
        for el in self.songs:
            return_list.append("== " + el.get_info())
        return_result = "\n".join(return_list)
        return f'Album {self.name}\n{return_result}'
