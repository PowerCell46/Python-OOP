class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        number_of_pages = photos_count // 4
        if number_of_pages * 4 == photos_count:
            return cls(number_of_pages)
        elif number_of_pages * 4 < photos_count:
            return cls(number_of_pages + 1)

    def add_photo(self, label: str):
        for index in range(len(self.photos)):
            page = self.photos[index]
            if len(page) < 4:
                page.append(label)
                return f'{label} photo added successfully on page {index + 1} slot'
        return f'No more free slots'

    def display(self):
        return_list = []
        return_list.append("-----------")
        for page in self.photos:
            return_list.append(" ".join(["[]" for ph in range(len(page))]))
            return_list.append("-----------")
        return "\n".join(return_list)
