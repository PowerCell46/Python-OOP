class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: str):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        free_rooms = []
        taken_rooms = []
        total_guests = 0
        for index in range(0, len(self.rooms)):
            room = self.rooms[index]
            total_guests += room.guests
            if room.is_taken:
                taken_rooms.append(str(index + 1))
            else:
                free_rooms.append(str(index + 1))
        return f'Hotel {self.name} has {total_guests} total guests\nFree rooms: {", ".join(free_rooms)}\nTaken rooms: {", ".join(taken_rooms)}'
