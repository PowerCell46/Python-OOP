class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def __delitem__(self, key):
        try:
            index = self.__keys.index(key)
            self.__keys[index] = None
            self.__values[index] = None
        except ValueError:
            raise KeyError('Invalid key!')

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("Invalid key!")

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def delete(self, key):
        del self[key]

    def __setitem__(self, key, value):
        if key in self.__keys:  # in case we are trying to change an already added key
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if len(self) == self.__max_capacity:  # in case the hash map is full
            self.__resize()

        index = self.__calculate_index(key)
        index = self.__get_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def add(self, key, value):
        self[key] = value

    def __calculate_index(self, key):  # hash function for creating an index
        return sum(ord(char) for char in key) % self.__max_capacity

    def __get_index(self, index):  # find free index
        if index == self.__max_capacity:
            index = 0

        if self.__keys[index] is None:
            return index
        return self.__get_index(index + 1)

    def __len__(self):  # get the number of free positions in the hash map
        return len([k for k in self.__keys if k is not None])

    def get_representation(self):
        print('{', end=' ')
        for i in range(self.__max_capacity):
            key = self.__keys[i]
            if key is not None:
                print(f'{key}: {self.__values[i]},', end=' ')
        print('}')

    def __resize(self):  # double the size of the hash map
        self.__keys = self.__keys + ([None] * self.__max_capacity)
        self.__values = self.__values + ([None] * self.__max_capacity)
        self.__max_capacity *= 2


# table = HashTable()
#
# table["name"] = "Peter"
#
# table["age"] = 25
#
# table.get_representation()
#
# table.delete('age')
#
# table.get_representation()
#
# print(table._HashTable__values)
