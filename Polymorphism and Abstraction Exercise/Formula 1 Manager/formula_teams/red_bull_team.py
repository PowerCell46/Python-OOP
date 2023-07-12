from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0
        if race_pos == 1:
            earned_money = 1_500_000 + 20_000
        elif race_pos == 2:
            earned_money = 800_000 + 20_000
        elif 2 < race_pos < 8:
            earned_money += 20_000
        elif race_pos == 8:
            earned_money = 20_000
        elif race_pos == 9:
            earned_money = 10_000
        elif race_pos == 10:
            earned_money = 10_000

        expenses_per_race = 250_000
        revenue = earned_money - expenses_per_race

        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'

