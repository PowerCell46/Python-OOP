from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos):
        earned_money = 0
        if race_pos == 1:
            earned_money = 1_000_000 + 100_000
        elif race_pos == 2:
            earned_money = 500_000 + 100_000
        elif race_pos == 3:
            earned_money = 500_000 + 100_000
        elif race_pos == 4:
            earned_money = 100_000
        elif race_pos == 5:
            earned_money = 100_000
        elif race_pos == 6:
            earned_money = 50_00
        elif race_pos == 7:
            earned_money = 50_000

        expenses_per_race = 200_000
        revenue = earned_money - expenses_per_race
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
