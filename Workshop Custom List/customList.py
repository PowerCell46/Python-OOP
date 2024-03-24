from __future__ import annotations


class CustomList:
    def __init__(self) -> None:
        self._data = []

    def append(self, value: int | str | float) -> [int | str | float]:
        self._data.append(value)
        return self._data

    def remove(self, index: int) -> int | str | float:
        return self._data.pop(index)

    def get(self, index: int) -> int | str | float:
        return self._data[index]

    def extend(self, lst) -> [int | str | float]:
        self._data.extend(lst)
        return self._data

    def insert(self, index: int, value: int | str | float) -> [int | str | float]:
        self._data.insert(index, value)
        return self._data

    def pop(self) -> int | str | float:
        return self._data.pop()

    def clear(self) -> None:
        self._data.clear()

    def index(self, value) -> int | str:
        return self._data.index(value)

    def count(self, value) -> int:
        return self._data.count(value)

    def reverse(self) -> [int | str | float]:
        self._data.reverse()
        return self._data

    def copy(self) -> CustomList:
        new_list = CustomList()
        new_list.extend(self._data)
        return new_list

    def size(self) -> int:
        return len(self._data)

    def add_first(self, value) -> None:
        self._data.insert(0, value)

    def dictionize(self) -> dict[int | str | float, int | str | float]:
        dictionary = {}
        flag = False
        for i in range(len(self._data)):
            if flag:
                flag = False
                continue
            elif i < len(self._data) - 1:
                dictionary[self._data[i]] = self._data[i + 1]
                flag = True
            else:
                dictionary[self._data[i]] = ' '
                break
        return dictionary

    def move(self, amount: int) -> [int | str | float]:
        if amount >= len(self._data):
            raise ValueError('Invalid amount!')
        self._data.extend(self._data[:amount])
        for i in range(amount):
            self._data.pop(0)
        return self._data

    def __calculate_custom_list_values(self) -> [int]:
        values_list = []
        for el in self._data:
            if isinstance(el, str):
                values_list.append(len(el))
            else:
                values_list.append(el)
        return values_list

    def sum(self) -> int | float:
        return sum(self.__calculate_custom_list_values())

    def overbound(self) -> int:
        if len(self._data) == 0:
            raise ValueError('No such value in an empty list!')
        custom_list_values = self.__calculate_custom_list_values()
        biggest_custom_list_value = sorted(custom_list_values, reverse=True)[0]
        return custom_list_values.index(biggest_custom_list_value)

    def underbound(self) -> int:
        if len(self._data) == 0:
            raise ValueError('No such value in an empty list!')
        custom_list_values = self.__calculate_custom_list_values()
        smallest_custom_list_value = sorted(custom_list_values)[0]
        return custom_list_values.index(smallest_custom_list_value)

    def __str__(self):
        return f'[{", ".join([str(el) for el in self._data])}]'


lst = CustomList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append('Hello')

# print(lst._CustomList__calculate_custom_list_values())
