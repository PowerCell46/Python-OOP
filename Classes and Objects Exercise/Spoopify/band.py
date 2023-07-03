class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.album_names = []

    def add_album(self, album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        self.album_names.append(album.name)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        if album_name not in self.album_names:
            return f'Album {album_name} is not found.'
        search_index = self.album_names.index(album_name)
        current_album = self.albums[search_index]
        if current_album.published:
            return f'Album has been published. It cannot be removed.'
        self.albums.pop(search_index)
        self.album_names.pop(search_index)
        return f'Album {album_name} has been removed.'

    def details(self):
        return_list = []
        for al in self.albums:
            return_list.append(al.details())
        return_result = "\n".join(return_list)
        return f'Band {self.name}\n{return_result}'
