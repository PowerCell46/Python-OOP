class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            return f'Player {player.name} joined team {self.__name}'
        else:
            return f'Player {player.name} has already joined'

    def remove_player(self, player_name):
        for player in self.__players:
            if player.name == player_name:
                search_index = self.__players.index(player)
                return self.__players.pop(search_index)
        return f'Player {player_name} not found'
