from prettytable import PrettyTable
from player import Player

table = PrettyTable()
my_player = Player()


class Players:
    def __init__(self):
        # self.players_name = ["Elie", "Peter", "Senso", "Miss. Fee", "Frank", "Adiddas"]
        self.players_name = []
        self.players_bids = []
        self.players_books = []
        self.players_points = []

    # Ask each player their names
    def ask_name(self, num):
        name = input(f"Player {num} name: ")
        self.players_name.append(name)
        my_player.name = name
        return my_player

    # Ask each player their bids
    def ask_bid(self):
        print("players_name: ", self.players_name)
        # for player in range(len(self.players_name)):
        #     current_player = self.players_name[player]
        #     bid = input(f"{current_player}, what's your bid? ")
        #     self.players_bids.append(my_player.add_bid(bid))

    # Ask each player their books
    def ask_books(self):
        for player in range(len(self.players_name)):
            current_player = self.players_name[player]
            books = int(input(f"{current_player}, what's your books? "))
            my_player.books = books
            points = my_player.calculate_points(self.players_bids[player], books)
            self.players_books.append(books)
            self.players_points.append(points)

    # Print the round points per player
    def print_table(self):
        table.add_column(f"Player Name", self.players_name)
        table.add_column(f"Bid", self.players_bids)
        table.add_column(f"Books", self.players_books)
        table.add_column(f"Points", self.players_points)
        print(table)
