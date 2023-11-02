
class Player:
    def __init__(self):
        self.name = ""
        self.bid = 0
        self.books = 0
        self.points = 0

    def add_bid(self, player_bid):
        # Did player go nil
        if str(player_bid) == "0":
            self.bid = 100
        # Did player go blind
        elif str(player_bid) == "b":
            self.bid = 200
        # Did player go normal
        else:
            self.bid = int(player_bid)
        return self.bid

    def calculate_points(self, current_bid, current_book):
        # Is the player's bid equal than player's books
        if current_bid == current_book:
            self.points = current_bid * 10
        # Is the player's bid greater than player's books
        elif current_bid > current_book:
            self.points = current_bid * -10
        # Is the player's bid less than player's books
        else:
            renaming_books = current_book - current_bid
            self.points = (current_bid * 10) + renaming_books
        return self.points

