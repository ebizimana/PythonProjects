from data import Players
from game import Game

print("Welcome to the Spades Books Keep App.")

my_data = Players()
the_game = Game()

# Ask for how many teams are playing
numberOfTeams = int(input("How many teams are playing? "))
the_game.number_of_teams = numberOfTeams

# Put the Players in their Team Name
the_game.divide_player()
print(the_game.team_names)

# while the_game.is_game_on():
#     # print(f"Round {the_game.round}. \n")
#     # Ask each player their bid
#     print(my_data.players_name)
#     my_data.ask_bid()
#
#     # Ask each player their books
#     # print("\n")
#     my_data.ask_books()
#     # Print the round points per player
#     # my_data.print_table()
#     # Increase the round
#     the_game.round += 1
#
#     # Only for Testing
#     the_game.highest_score = 500



