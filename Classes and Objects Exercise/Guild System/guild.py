class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.name_of_the_players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != "Unaffiliated":
            return f'Player {player.name} is in another guild.'
        player.guild = self.name
        self.players.append(player)
        self.name_of_the_players.append(player.name)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        if player_name not in self.name_of_the_players:
            return f'Player {player_name} is not in the guild.'
        search_index = self.name_of_the_players.index(player_name)
        self.name_of_the_players.pop(search_index)
        current_player = self.players.pop(search_index)
        current_player.guild = "Unaffiliated"
        return f'Player {current_player.name} has been removed from the guild.'

    def guild_info(self):
        return_list = []
        for el in self.players:
            return_list.append(el.player_info())
        return_result = "\n".join(return_list)
        return f'Guild: {self.name}\n{return_result}'
