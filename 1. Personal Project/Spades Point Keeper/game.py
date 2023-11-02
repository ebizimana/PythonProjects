from team import Team

my_team = Team()

class Game:
    def __init__(self):
        self.score = 500
        self.round = 1
        self.bags_per_round = 20
        self.number_of_teams = 0
        self.highest_score = 0
        self.team_names = []
        self.teams = []
        self.team_accumulating_score = []

    # Divide the players in teams
    def divide_player(self):
        """Puts the players in Teams outputs team object"""
        # Repeat until there is no more teams
        for team in range(self.number_of_teams):
            # Ask for the name for team
            team_name = my_team.ask_team_name(team+1)
            self.team_names.append(team_name)
            # Ask the names of the players for that team
            players_in_the_team = my_team.ask_team_players()
            self.teams.append(players_in_the_team)
            print("\n")

    # Keep Playing
    def is_game_on(self):
        if self.highest_score >= 500:
            return False
        elif len(self.team_accumulating_score) == 0:
            return True
        else:
            for team in range(self.number_of_teams):
                current_score = self.team_accumulating_score[team]
                if self.highest_score < current_score:
                    self.highest_score = current_score
                    return True

    # TODO: Calculate each the team round score
    # def calculate_team_score(self):
