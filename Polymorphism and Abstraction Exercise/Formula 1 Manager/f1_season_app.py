from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name != "Red Bull" and team_name != "Mercedes":
            raise ValueError("Invalid team name!")
        elif team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        return f'{team_name} has joined the new F1 season.'

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team == None or self.mercedes_team == None:
            raise Exception("Not all teams have registered for the season.")
        winner = None
        if red_bull_pos < mercedes_pos:
            winner = "Red Bull"
        elif mercedes_pos < red_bull_pos:
            winner = "Mercedes"
        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        return f'Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. {winner} is ahead at the {race_name} race.'
