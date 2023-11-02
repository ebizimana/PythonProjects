from data import Players

my_players = Players()


class Team:
    def __init__(self):
        self.name = ""
        self.players_in_team = []
        self.team_score = 0

    def ask_team_name(self, num):
        team_name = input(f"Team {num} Name: ")
        self.name = team_name
        return self.name

    def ask_team_players(self):
        for num in range(2):
            player = my_players.ask_name(num+1)
            self.players_in_team.append(player)
        return self.players_in_team

    def calculate_team_score(self, players):
        for player in range(len(players.players_name)):
            self.team_score += players.players_points
